import os 
import sys
import logs
import datetime as dt

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV
from settings.constants import CouchbaseConstants, ElasticsearchConstants

#from pipeline.couchbase_n1ql import get_all 
from pipeline import couchbase_n1ql
from pipeline import couchbase_sync
from pipeline import transform
from pipeline import elastic

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

def oldcuris2elastic():
    cb_constants = CouchbaseConstants
    es_constants = ElasticsearchConstants
    cb_data = couchbase_n1ql.get_all(cb_constants['philippines'])
    etl_data = transform.init_pipeline(cb_data)
    result = elastic.bulk_dump(etl_data, es_constants['country']['philippines'])

def main():
    oldcuris2elastic()

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

