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

conn = CouchbaseConfig[CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"

def get_all(country): 
    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT 

        statement = _set_statement(country=country)
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

    return ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                + BUCKET + ".* FROM "
                + BUCKET + " WHERE address.country='"
                + country + "' AND _deleted IS MISSING AND type='user-resident'")

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    return data

#run as standalone module
if __name__ == "__main__":
    get_all()
    