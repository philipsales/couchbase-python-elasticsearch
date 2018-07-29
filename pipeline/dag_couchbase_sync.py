import json
import os 
import sys
import requests

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError
from couchbase.exceptions import CouchbaseNetworkError
from requests.exceptions import ConnectionError, RequestException 

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV

import logs.logging_conf, logging
logger = logging.getLogger("couchbase.syncgateway")

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

conn = CouchbaseConfig[CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUTE = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"

def task2():
    print('hello')

def init_couchbase():
    headers = _conn_headers()
    filters = _conn_filters()
    url = _conn_url()

    try:
        r = requests.get(url, headers = headers, params = filters)
        logger.info(r.status_code)
        logger.info(r.elapsed.total_seconds())
        #logger.info(r.text)

    except (ConnectionError, RequestException, CouchbaseNetworkError) as err: 
        logger.error(err)
        sys.exit(1)

def _conn_headers(**kwargs):
    #TODO make dynamic pass kwargs
    return {
        "accept": "application/json",
        "allow_redirects": "True",
        "timeout": str(TIMEOUTE),
    }

def _conn_filters(**kwargs):
    #TODO make dynamic pass kwargs
    return  {
        "access" : "false",
        "channels": "false",
        "include_docs": "true",
        "revs": "false",
        "update_seq": "false",
        "limit": "10"
    }

def _conn_url(**kwargs):
    protocol = PROTOCOL
    ip_address = IP_ADDRESS
    port = PORT 
    bucket = BUCKET
    api_endpoint = API_ENDPOINT 

    urls = protocol + "://"  + ip_address + ":" + port + "/"  + bucket + "/" + api_endpoint  
    logger.info(urls)
    return urls

if __name__ == "__main__":
    init_couchbase()
    
default_args = {
    'owner': 'Philip',
    'start_date': dt.datetime(2017, 6, 1)
}

with DAG('foobar',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    task1 = PythonOperator(task_id='task1', 
            python_callable=init_couchbase)

    task2 = PythonOperator(task_id='task2', 
            python_callable=task2)

    task1 >> task2

