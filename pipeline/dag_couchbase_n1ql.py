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
logger = logging.getLogger("couchbase.n1q1")

import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

conn = CouchbaseConfig[CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"

def task2():
    print('hello')

def get_all(): 
    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT 

        statement = _set_statement()
        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 

        res = bucket.n1ql_query(query) 
        logger.info(res)

        return _dict2json(res)

    except (RequestException, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.error(err)
        sys.exit(1) 

def _set_statement(**kwargs):
    return ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                + BUCKET + ".* FROM "
                + BUCKET + " limit 10")

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    return data

if __name__ == "__main__":
    get_all()
    
default_args = {
    'owner': 'Philip',
    'start_date': dt.datetime(2017, 6, 1)
}

with DAG('dg_couchbase_n1ql',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    t_get_all = PythonOperator(task_id='t_get_all', 
            python_callable=get_all)


