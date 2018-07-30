import os 
import sys

import logs

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV 

from pipeline.couchbase_syncgateway import SyncGatewayConnect 
from pipeline.couchbase_n1ql import N1QLConnect 
from pipeline.elasticsearch import ElasticsearchConnect 
from pipeline.transform import CurisV2ETL

from pipeline.dag_couchbase_sync import init_couchbase 

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def main1():
    cb = init_couchbase() 

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

    es_conn = ElasticSearchConfig[ElasticSearchENV]
    es = ElasticsearchConnect(es_conn)
    es.bulk_dump(es_data)

if __name__ == '__main__':
    main()

  
default_args = {
    'owner': 'Philip',
    'start_date': dt.datetime(2017, 6, 1)
}

with DAG(dag_id='main_dag',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    main1 = PythonOperator(task_id='main1', 
            python_callable=main1)

    main1 
