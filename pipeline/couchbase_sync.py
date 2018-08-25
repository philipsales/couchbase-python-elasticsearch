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

conn = CouchbaseConfig[CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUTE = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_changes?"

def init_couchbase():
    headers = _conn_headers()
    filters = _conn_filters()
    url = _conn_url()

    try:
        r = requests.get(url, headers = headers, params = filters)
        logger.info(r.status_code)
        logger.info(r.elapsed.total_seconds())
        logger.info(r.json())
        return _dict2json(r.json()["results"])

    except (ConnectionError, RequestException, CouchbaseNetworkError) as err: 
        logger.error(err) 
        sys.exit(1)

def _conn_headers():
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
        "limit":"5",
        "since":"200"
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

def _dict2json(results):
    counter = 0
    data = []

    for row in results: 
        doc = row["doc"]
        doc["cb_id"] = doc.pop('_id')
        data.append(json.dumps(doc))
        counter += 1
        logger.info(counter)

    return data