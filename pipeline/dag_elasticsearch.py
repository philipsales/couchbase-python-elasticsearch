import uuid
import json
import logging

import mappings.schema

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError 

import logs.logging_conf, logging
logger = logging.getLogger("elasticsearch.connection")

from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV 

conn = ElasticSearchConfig[ElasticSearchENV]

INDEX = conn['INDEX']
DOC_TYPE = conn['TYPE']
HOST1 = conn['HOST']
HOST2 = conn['HOST']
nodes = [HOST1, HOST2]

es = Elasticsearch( 
    nodes,
    http_auth = (conn['USERNAME'], conn['PASSWORD']),
    scheme = conn['SCHEME'],
    port = conn['PORT'],
    timeout = int(conn['TIMEOUT']))

"""
test_docs = [
'{"address": {"community": "Puerta", "province": "Palawan", "zip": "5009"}}',
'{"address": {"community": "Iligan", "province": "Cebu", "zip": "5008"}}',
'{"address": {"community": "Puerto", "province": "Princesa", "zip": "5009"}}'
]
"""

def bulk_dump(docs):
    set_mappings()
    counter = 0

    bulk_data = []
    
    try:
        #for doc in test_docs:
        for doc in docs:
            logger.info(doc)
            _header = { "create" : { "_index" : INDEX,  
                        "_type" : DOC_TYPE, 
                        "_id" : str(uuid.uuid1()) } }

            bulk_data.append(json.dumps(_header))
            bulk_data.append(doc)
            counter += 1

            #bulk_data = ['{"create": {"_index": "philippines", "_type": "patients", "_id": "'+ str(uuid.uuid1()) +'"}}', '{"address": {"community": "Iligan", "province": "Cebu", "zip": "5008"}}']
        logger.info(bulk_data)
        return es.bulk(bulk_data)

    except (ConnectionError) as err: 
        logger.error(error)

def set_mappings():
    body = mappings.schema.elastic_mapping

    if es.indices.exists(INDEX):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = INDEX, 
                                    body = json.dumps(body))

            print(" response: '%s'" % (res))

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)

if __name__ == "__main__":
    bulk_dump(data)
  