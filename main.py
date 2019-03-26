import os 
import sys
import logs
import json
import pprint
import datetime as dt

import lib.logs.logging_conf, logging
logger = logging.getLogger("main.py")

from settings.base_conf import ELASTICSEARCH, COUCHBASE
from settings.base_conf import elastic_config, couchbase_config 

from pipeline.extract import couchbase_n1ql, couchbase_sync, elastic, kobo, sqlite

from pipeline.transform import transformer

PHILIPPINES = 'philippines'
CAMBODIA = 'cambodia'


def extract_data():
    cb_data = couchbase_sync.init_couchbase()
    # cb_data = couchbase_n1ql.couchbase_get(COUCHBASE['philippines'])
    return cb_data

def transform_data(**kwargs):
    cb = kwargs['ti']
    cb_data = cb.xcom_pull(task_ids='extract_from_couch')
    etl_data = transformer.init_pipeline(cb_data)
    return etl_data

def load_data(**kwargs):
    transform_data = kwargs['ti']
    etl_data = transform_data.xcom_pull(task_ids='transform_couch_data')
    result = elastic.bulk_dump(etl_data)
    return result 

def newAQMkobo2elastic(country):
    kobo_data = kobo.kobo_get_stream()

def kobo2oldcuris():
    kobo_data = kobo.kobo_get()
    etl_data = transformer.kobo2oldcuris(kobo_data)
    return couchbase_sync.push_couchbase(etl_data)

def oldcuris2elastic(country):
    cb_data = couchbase_n1ql.couchbase_get(COUCHBASE[country])
    etl_data = transformer.oldcuris2elastic(cb_data)
    return elastic.set_json_dump(etl_data, ELASTICSEARCH['country'][country])

def main():
    logger.info('main')
    #newAQMkobo2elastic(PHILIPPINES)
    #kobo2oldcuris()
    #oldcuris2elastic(PHILIPPINES)
    oldcuris2elastic(CAMBODIA)
    

#run as standalone package
if __name__ == '__main__':
    main()

#run as workflow 