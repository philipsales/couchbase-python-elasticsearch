import os 
import sys

import logs

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV 

from pipeline.couchbase_syncgateway import SyncGatewayConnect 
from pipeline.couchbase_n1ql import N1QLConnect 
from pipeline.dag_couchbase_n1ql import get_all 

from pipeline.elastic import ElasticsearchConnect 
from pipeline.transform import CurisV2ETL

from pipeline.dag_couchbase_sync import init_couchbase 
from pipeline.dag_couchbase_n1ql import get_all 
from pipeline.dag_elasticsearch  import bulk_dump 
from pipeline.dag_transform import init_pipeline

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def extract_data():
    cb_data = get_all()
    return cb_data

def transform_data(**kwargs):
    ti = kwargs['ti']
    print('ti = kwargs !!!!!!!!!!!')
    path = ti.xcom_pull(task_ids='t_extract_data')
    print('from extract data !!!!!!!!!!!!!!!')
    print(path)
    etl_data = init_pipeline(path)
    print('result from init_pipeline !!!!!!!!!!!!!!')
    print(etl_data)
    return etl_data

def load_data(**kwargs):
    ti = kwargs['ti']
    print('ti = kwargs !!!!!!!!!!!')
    path = ti.xcom_pull(task_ids='t_transform_data')
    print('from transfomr data !!!!!!!!!!!')
    print(path)
    etl_data = bulk_dump(path)
    print('- result of bulk_data !!!!!!!')
    print(etl_data)
    return etl_data

def main():
    cb_conn = CouchbaseConfig[CouchbaseENV]
    """
    cb = SyncGatewayConnect(cb_conn)
    cb_data = cb.get_all()
    """

    cb = N1QLConnect(cb_conn)
    cb_data = cb.get_all()

    etl = CurisV2ETL()
    es_data = etl.map_address(cb_data)

    es_conn = ElasticSearchConfig['development']
    es = ElasticsearchConnect(es_conn)
    es.bulk_dump(es_data)


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

    t_extract_data = PythonOperator(task_id='t_extract_data', 
            python_callable=extract_data)

    t_transform_data = PythonOperator(task_id='t_transform_data', 
            provide_context=True,
            depends_on_past=True,
            python_callable=transform_data)

    t_load_data = PythonOperator(task_id='t_load_data', 
            depends_on_past=True,
            provide_context=True,
            python_callable=load_data)

    #t_extract_data.set_downstream(t_transform_data)
    #t_transform_data.set_downstream(t_load_data)

t_extract_data >> t_transform_data >> t_load_data

