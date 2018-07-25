import os 
import sys

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root +'/logs')
sys.path.append(root +'/settings')

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError
from couchbase.exceptions import CouchbaseNetworkError

import json
import requests

from requests.exceptions import RequestException

from couchbase_conf import CouchbaseConfig, CouchbaseENV

import logging_conf, logging
logger = logging.getLogger("couchbase.n1q1")

class N1QLConnect:
    
    def __init__(self, conn=[], **kwargs):

        if not conn:
            cb_ENV = CouchbaseENV
            conn = CouchbaseConfig[cb_ENV]

        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._ip_address = conn['IP'] 
        self._timeout = conn['TIMEOUT']

    def get_all(self):
        try:
            bucket = Bucket(self._url)
            bucket.n1ql_timeout = self._timeout 

            script = self._set_query()
            query = N1QLQuery(script)
            query.timeout = self._timeout 

            res = bucket.n1ql_query(query) 
            logger.info(res)

            return self._dict2json(res)

        except (ConnectionError, 
                RequestException, 
                CouchbaseTransientError,
                CouchbaseNetworkError) as err: 
            logger.error(err)
            sys.exit(1)

    def _set_query(self, **kwargs):

        return ("SELECT meta(" + self._bucket + ").id as cb_id, " 
                 + self._bucket + ".* FROM "
                 + self._bucket + " limit 10")

    def _dict2json(self, results):
        counter = 0
        data = []

        for row in results: 
            data.append(json.dumps(row))
            counter += 1
            logger.info(counter)

        return data

    def find(self):
        pass:

    def get_changes(self):
        pass:

if __name__ == '__main__':
    N1QLConnect().get_all()


