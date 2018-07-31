import sys 
import uuid
import json
import logging

from mappings import schema

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

def bulk_dump(docs):
    set_mappings()
    counter = 0
    bulk_data = []
    
    try:
        for doc in docs:
            _type = list(doc.keys())
            _body = list(doc.values())

            _header = { "create" : { "_index" : INDEX,  
                        "_type" : _type[0], 
                        "_id" : str(uuid.uuid1()) } }

            bulk_data.append(_header)
            bulk_data.append(_body[0])
            counter += 1

        logger.info(bulk_data)
        return es.bulk(bulk_data)

    except (ConnectionError) as err: 
        logger.error(error)

def batch_dump(docs):
        set_mappings()
        counter = 0

        try:
            for doc in docs:
                _type = list(doc.keys())
                _body = list(doc.values())

                res = es.index(index = INDEX, 
                         doc_type = _type[0] , 
                         id = uuid.uuid1(), 
                         body = _body[0])
                counter += 1

            _total_entries(counter)
            _refresh_index(INDEX)

        except (ConnectionError) as err: 
            logger.error(error)

def _refresh_index(data):
    return es.indices.refresh(index=data)

def _total_entries(count):
    print("Total Batch Entries: {%}", count)

def set_mappings():
    all_mappings = {}
    all_mappings.update(schema.profile_mapping)
    all_mappings.update(schema.health_mapping)
    all_mappings.update(schema.household_mapping)
    all_mappings.update(schema.symptoms_mapping)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'

    if es.indices.exists(INDEX):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = INDEX, body = body )
            logger.info(res)

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)

#run as standalone module
if __name__ == "__main__":
    bulk_dump(data)
  