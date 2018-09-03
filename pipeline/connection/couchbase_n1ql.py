import json
import os 
import sys
import requests
import datetime as dt

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError
from couchbase.exceptions import CouchbaseNetworkError
from requests.exceptions import ConnectionError, RequestException 

import logs.logger as lg

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.base_conf import LoggerConstants

import logs.logging_conf, logging
logger = logging.getLogger("couchbase.n1q1")

conn = CouchbaseConfig[CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"

_log_file_name = LoggerConstants['filenames']['etl']

def _couchbase_get(country):
    try:
        sync_date = lg._get_last_batch_log(_log_file_name)

        statement = _set_statement(type='batch',country=country,sync_date=sync_date)

        logger.info(statement)
        
    except FileNotFoundError:
        statement = _set_statement(type='initial',country=country)
        logger.info(statement)

    res = get_all(statement, country)
    return _dict2json(res)

def get_all(statement, country): 
    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT

        lg.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        lg.write_to_log("Query: " + statement + "; ", _log_file_name)

        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 

        res = bucket.n1ql_query(query)

    except (RequestException, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.error(err)
        sys.exit(1)

    return res

def _set_statement(**kwargs):
    query_type = kwargs.get('type', "")
    country = kwargs.get('country',"")

    if query_type=="initial":
        query = ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                    + BUCKET + ".* FROM "
                    + BUCKET + " WHERE address.country='"
                    + country + "' AND _deleted IS MISSING AND type='user-resident'")
    elif query_type=="batch":
        date_sync = kwargs.get('sync_date', "")

        query = ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                    + BUCKET + ".* FROM "
                    + BUCKET + " WHERE address.country='"
                    + country + "' AND _deleted IS MISSING AND type='user-resident' AND _sync.time_saved LIKE '"
                    + date_sync + "%'")

    return query
    # return ("SELECT meta(" + BUCKET + ").id as cb_id, " 
    #                 + BUCKET + ".* FROM "
    #                 + BUCKET + " WHERE address.country='"
    #                 + country + "' AND _deleted IS MISSING AND type='user-resident' LIMIT 20")

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    lg.write_to_log("Count From Couchbase: " + str(counter) + "; ", _log_file_name)

    return data

#run as standalone module
if __name__ == "__main__":
    get_all()
    