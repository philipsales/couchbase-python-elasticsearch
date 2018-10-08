import os 
import sys
import logs
import json
import datetime as dt

from settings.base_conf import ELASTICSEARCH, COUCHBASE
from settings.base_conf import elastic_config, couchbase_config 

from pipeline.connection import couchbase_n1ql, couchbase_sync, elastic, kobo, sqlite

from pipeline.transformation import transform

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

PHILIPPINES = 'philippines'
CAMBODIA = 'cambodia'


def extract_data():
    cb_data = couchbase_sync.init_couchbase()
    # cb_data = couchbase_n1ql.couchbase_get(COUCHBASE['philippines'])
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
    kobo_data = kobo.kobo_get()
    etl_data = transform.kobo2oldcuris(kobo_data)
    print(etl_data)
    # result = couchbase_sync.push_couchbase(etl_data)

def oldcuris2elastic(country):
    cb_data = couchbase_n1ql.couchbase_get(COUCHBASE[country])
    etl_data = transform.oldcuris2elastic(cb_data)
    elastic.set_json_dump(etl_data, ELASTICSEARCH['country'][country])

def main():
    kobo2oldcuris()
    # oldcuris2elastic(PHILIPPINES)
    # oldcuris2elastic(CAMBODIA)
    

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

