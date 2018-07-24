import json

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery
from couchbase.n1ql import N1QLError

class SyncGatewayConnect:
    def __init__(self, conn, **kwargs):
        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._timeout = conn['TIMEOUT']

    def get_all(self):
        pass

    def get_changes(self):
        pass

    def find(self):
        pass

class N1QLConnect:
    
    def __init__(self, conn, *args,**kwargs):
        self._bucket = conn['BUCKET'] 
        self._url = conn['HOST'] + conn['BUCKET']
        self._timeout = conn['TIMEOUT']

    def get_all(self):
        counter = 0
        cb_data = []

        bucket = Bucket(self._url)
        bucket.n1ql_timeout = self._timeout 
        
        try:
            query = N1QLQuery("SELECT meta("+self._bucket+").id as cb_id, " 
                              + self._bucket + ".* FROM "
                              + self._bucket +" limit 30")

            query.timeout = self._timeout 

            for row in bucket.n1ql_query(query): 
                cb_data.append(json.dumps(row))
                counter += 1
                print('--couchbase: ', counter)

            return cb_data

        except:
            #TODO
            pass

    def get_changes(self):
        pass


