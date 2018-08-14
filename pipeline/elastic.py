import sys 
import uuid
import json
import logging

from schemas.output import elastic_schema
from settings import constants

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

def bulk_dump(docs, country):
    create_mappings(country)
    counter = 0
    bulk_data = []
    
    try:
        for doc in docs:
            try:
                _type = list(doc.keys())
                _body = list(doc.values())

                index = _set_index(country,_type[0])

                _header = { "create" : { "_index" : index,  
                            "_type" : _type[0], 
                            "_id" : str(_body[0]["awh_id"]) } }

                bulk_data.append(_header)
                bulk_data.append(json.dumps(_body[0]))
                counter += 1
            except TypeError:
                print("NoneType object!")
                continue

        logger.info(bulk_data)
        return es.bulk(bulk_data)
            
    except (ConnectionError) as err: 
        logger.error(error)

def _refresh_index(data):
    return es.indices.refresh(index=data)

def _total_entries(count):
    print("Total Batch Entries: {%}", count)

def create_mappings(country):
    # Crate mapping for demographics
    _set_mappings(country, constants.ElasticsearchConstants['index']["demographics"])
    # Crate mapping for household
    _set_mappings(country, constants.ElasticsearchConstants['index']["household"])
    # Crate mapping for health
    _set_mappings(country, constants.ElasticsearchConstants["index"]["health"])
    # Crate mapping for symptoms
    _set_mappings(country, constants.ElasticsearchConstants["index"]["symptoms"])

def _set_mappings(country, index):
    all_mappings = manage_mapping(index)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'
    main_index = _set_index(country, index)

    if es.indices.exists(main_index):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = main_index, body = body )
            logger.info(res)

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)


def _set_index(country, schema):
    return (constants.ElasticsearchConstants['country'][country] 
            + "_" + constants.ElasticsearchConstants['index'][schema])

def manage_mapping(index):
    if index == constants.ElasticsearchConstants["index"]["demographics"]:
        return elastic_schema.profile_mapping
    elif index == constants.ElasticsearchConstants["index"]["health"]:
        return elastic_schema.health_mapping
    elif index == constants.ElasticsearchConstants["index"]["household"]:
        return elastic_schema.household_mapping
    elif index == constants.ElasticsearchConstants["index"]["symptoms"]:
        return elastic_schema.symptoms_mapping

#run as standalone module
if __name__ == "__main__":
    bulk_dump(data)