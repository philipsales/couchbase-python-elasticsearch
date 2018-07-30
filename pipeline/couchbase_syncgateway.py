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

class SyncGatewayConnect:

    def __init__(self, conn=[], **kwargs):
        if not conn:
            cb_ENV = CouchbaseENV
            conn = CouchbaseConfig[cb_ENV]

        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._ip_address = conn['IP'] 
        self._timeout = conn['TIMEOUT']
        self._protocol = conn['PROTOCOL']
        self._port = conn['PORT']
        self._api_endpoint = "_all_docs?"

    def get_all(self):
        headers = self._conn_headers()
        filters = self._conn_filters()
        url = self._conn_url()

        try:
            r = requests.get(url, headers = headers, params = filters)
            logger.info(r.status_code)
            logger.info(r.elapsed.total_seconds())

        except (ConnectionError, RequestException, CouchbaseNetworkError) as err: 
            logger.error(err)
            sys.exit(1)

    def _conn_headers(self, *kwargs):
        #TODO make dynamic thru kwargs
        return {
            "accept": "application/json",
            "allow_redirects": "True",
            "timeout": str(self._timeout),
        }

    def _conn_filters(self, *kwargs):
        #TODO make dynamic thru kwargs
        return  {
            "access" : "false",
            "channels": "false",
            "include_docs": "true",
            "revs": "false",
            "update_seq": "false",
            "limit": "2"
        }

    def _conn_url(self, *kwargs):
        protocol = self._protocol
        ip_address = self._ip_address
        port = self._port 
        bucket = self._bucket
        api_endpoint = self._api_endpoint 

        urls = protocol + "://"  + ip_address + ":" + port + "/"  + bucket + "/" + api_endpoint  
        return urls

    def get_changes(self):
        pass

    def find(self):
        pass

if __name__ == '__main__':
    SyncGatewayConnect().get_all()
