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
from settings.constants import LoggerConstants

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

_log_file_name = LoggerConstants['filename']['etl']

def get_all(country): 
    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT 

        sync_date = lg._get_last_batch_log(_log_file_name)

        statement = _set_statement(country=country,sync_date=sync_date)

        lg.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        lg.write_to_log("query: " + statement + "; ", _log_file_name)

        logger.info(statement)
        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 

        res = bucket.n1ql_query(query)

        return _dict2json(res)

    except (RequestException, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.error(err)
        sys.exit(1)

def _set_statement(**kwargs):
    country = kwargs.get('country',"")
    date_sync = kwargs.get('sync_date', "")

    return ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                + BUCKET + ".* FROM "
                + BUCKET + " WHERE address.country='"
                + country + "' AND _deleted IS MISSING AND type='user-resident' AND _sync.time_saved LIKE '"
                + date_sync + "%'")

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    lg.write_to_log("count from couchbase: " + str(counter) + "; ", _log_file_name)

    return data

#run as standalone module
if __name__ == "__main__":
    get_all()
    