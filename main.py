import os 
import sys
import logs
import json
import datetime as dt

from settings.base_conf import ELASTICSEARCH_CONSTANTS, COUCHBASE_CONSTANTS, SQLITE_DATABASE
from settings.base_conf import elastic_config, couchbase_config 

from pipeline.auxiliary import sqlite_checker

from pipeline.connection import couchbase_n1ql, couchbase_sync, elastic, kobo, sqlite

from pipeline.transformation import transform

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def extract_data():
    cb_data = couchbase_sync.init_couchbase()
    # cb_constants = CouchbaseConstants
    # cb_data = couchbase_n1ql.get_all(cb_constants['philippines'])
    return cb_data

def transform_data(**kwargs):
    cb = kwargs['ti']
    cb_data = cb.xcom_pull(task_ids='extract_from_couch')
    etl_data = transform.init_pipeline(cb_data)
    return etl_data

def load_data(**kwargs):
    transform_data = kwargs['ti']
    etl_data = transform_data.xcom_pull(task_ids='transform_couch_data')
    result = elastic.bulk_dump(etl_data)
    return result 

def kobo2oldcuris():
    kobo_data = kobo._kobo_get()
    etl_data = transform.kobo2oldcuris(kobo_data)

    conn = sqlite.create_connection(SQLITE_DATABASE) 
    sqlite._create_table(conn) 
    sqlite_data = sqlite_checker.segregate_ids(conn,etl_data)
    
    result = couchbase_sync.push_couchbase(sqlite_data)
    sqlite._close_db(conn)

def oldcuris2elastic():
    cb_data = couchbase_n1ql._couchbase_get(COUCHBASE_CONSTANTS['philippines'])
    etl_data = transform.oldcuris2elastic(cb_data)
    elastic._set_json_dump(etl_data, ELASTICSEARCH_CONSTANTS['country']['philippines'])

def main():
    oldcuris2elastic()
    # kobo2oldcuris()

#run as standalone package
if __name__ == '__main__':
    main()

#run as workflow 
default_args = {
    'owner': 'ELKadmin',
    'start_date': dt.datetime(2017, 6, 1)
}

with DAG(dag_id='dg_main',
    default_args=default_args,
    schedule_interval='0 1 * * *',
    ) as dag:

    extract_from_couch = PythonOperator(task_id='extract_from_couch', 
            python_callable=extract_data)

    transform_couch_data = PythonOperator(task_id='transform_couch_data', 
            provide_context=True,
            depends_on_past=True,
            python_callable=transform_data)

    load_to_elasticsearch = PythonOperator(task_id='load_to_elasticsearch', 
            depends_on_past=True,
            provide_context=True,
            python_callable=load_data)

extract_from_couch >> transform_couch_data >> load_to_elasticsearch

