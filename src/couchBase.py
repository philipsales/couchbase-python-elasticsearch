import json

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery
from couchbase.n1ql import N1QLError

class CouchbaseConnect:
    
    def __init__(self, conn, **kwargs):
        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._timeout = conn['TIMEOUT']

    def curl_all(self):
        pass

    def gateway_sync_all(self):
        pass

    def n1ql_all(self):
        counter = 0
        cb_data = []

        bucket = Bucket(self._url)
        bucket.n1ql_timeout = self._timeout 
        
        try:
            query = N1QLQuery("SELECT meta("+self._bucket+").id as cb_id, " 
                              + self._bucket + ".* FROM "
                              + self._bucket +" limit 10")

            query.timeout = self._timeout 

            for row in bucket.n1ql_query(query): 
                cb_data.append(json.dumps(row))
                counter += 1
                print('--couchbase: ', counter)

            return cb_data

        except:
            #TODO
            pass



