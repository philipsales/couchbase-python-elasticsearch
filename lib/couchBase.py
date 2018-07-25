
import json
import time
import requests

import os 
import sys

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root +'/settings')
sys.path.append(root +'/logs')

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError, CouchbaseNetworkError

from requests.exceptions import RequestException

import config
from log_config import main, logging
logger = logging.getLogger("couchbase.connection")


class SyncGatewayConnect:

    def __init__(self, conn=[], **kwargs):

        if not conn:
            cb_ENV = 'dev'
            conn = config.CouchbaseConfig[cb_ENV]

        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._ip_address = conn['IP'] 
        self._timeout = conn['TIMEOUT']

        headers = self._conn_headers()
        filters = self._conn_filters()
        url = self._conn_config()

        try:
            r = requests.get(url, headers = headers, params=filters)
            logger.info(r.status_code)
            logger.info(r.elapsed.total_seconds())

        except RequestException as err: 
            logger.error(err)

    def _conn_headers(self, *kwargs):

        return {
            "accept": "application/json",
            "allow_redirects": "True",
            "timeout": str(self._timeout),
        }

    def _conn_filters(self, *kwargs):

        return  {
            "access" : "false",
            "channels": "false",
            "include_docs": "true",
            "revs": "false",
            "update_seq": "false",
            "limit": "10"
        }

    def _conn_config(self, *kwargs):
        ip_address = self._ip_address
        bucket = self._bucket
        scheme = "http"
        port = "4984"
        api_endpoint = "_all_docs?"

        return scheme + "://"  + ip_address + ":" + port + "/"  + bucket + "/" + api_endpoint  

    def get_changes(self):
        pass

    def find(self):
        pass

class N1QLConnect:
    
    #def __init__(self, conn, *args,**kwargs):
    def get_all(self, conn, *args,**kwargs):
        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._timeout = conn['TIMEOUT']

        try:
            bucket = Bucket(self._url)
            bucket.n1ql_timeout = self._timeout 

            script = self._set_query()

            query = N1QLQuery(script)
            query.timeout = self._timeout 

            res = bucket.n1ql_query(query) 
            logger.info(res)

            return self._dict2json(res)

        except CouchbaseTransientError as err: 
            logger.error(err)
        except CouchbaseNetworkError as err: 
            logger.error(err)

    def _set_query(self, **kwargs):

        return ("SELECT meta("+self._bucket+").id as cb_id, " 
                 + self._bucket + ".* FROM "
                 + self._bucket +" limit 10")

    def _dict2json(self, results):
        counter = 0
        data = []

        for row in results: 
            data.append(json.dumps(row))
            counter += 1
            logger.info(counter)

        return data

if __name__ == '__main__':
    SyncGatewayConnect()

