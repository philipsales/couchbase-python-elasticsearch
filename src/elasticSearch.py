import sys
import uuid
import json

import mappings.schema

from elasticsearch import Elasticsearch

class ElasticsearchConnect:

    def __init__(self, conn, *args,**kwargs):
        self._index = conn['INDEX']
        self._doc_type = conn['TYPE']
        self._es = Elasticsearch(
            conn['HOST'],
            http_auth=(conn['USERNAME'],conn['PASSWORD']),
            scheme=conn['SCHEME'],
            port=conn['PORT'],
            timeout=conn['TIMEOUT'])
            
    def batch_dump(self, docs):
        self._set_mappings()
        counter = 0

        try:
            for doc in docs:
                res = self._es.index(index = self._index, 
                                     doc_type = self._doc_type, 
                                     id = uuid.uuid1(), 
                                     body = doc)
                counter += 1

            self._total_entries(counter)
            self._es.indices.refresh(index=self._index)
            self._refresh_index()

        except:
            pass

    def bulk_dump(self, docs):
        self._set_mappings()
        counter = 0
        bulk_data = []

        try:
            for doc in docs:
                _header = { "create" : { "_index" : self._index,  
                            "_type" : self._doc_type, 
                            "_id" : str(uuid.uuid1()) } 
                          }
                bulk_data.append(json.dumps(_header))
                bulk_data.append(doc)
                counter += 1
                print('--elastic: ', counter)

            self._total_entries(counter)
            return self._es.bulk(bulk_data)

        except:
            pass

    def get_total(self):
        query = self._es.search(index = self._index, 
                                body = {"query": {"match_all": {}}})

        print("Total Elastic records %d Hits:" % query['hits']['total'])

    def _set_mappings(self):
        body = mappings.schema.elastic_mapping

        if self._es.indices.exists(self._index):
            print('index exist')
        else:
            try: 
                res = self._es.indices.create(index = self._index, 
                                              body = json.dumps(body))
                print(" response: '%s'" % (res))
                if res["acknowledged"] != True:
                    print("Index creation failed...")
                else:
                    print("Index created...")

            except:
                pass

    def _refresh_index(self):
        return self._es.indices.refresh(index=self._index)

    def _total_entries(self,count):
        print("Total Batch Entries: ", count)



