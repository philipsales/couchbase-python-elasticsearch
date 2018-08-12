import sys 
import uuid
import json
import logging

from mappings import schema
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
    set_mappings(country)
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

def set_mappings(country):
    _set_demographics(country)
    _set_household(country)
    _set_health(country)
    _set_symptoms(country)


def _set_index(country, schema):
    return (constants.ElasticsearchConstants['country'][country] 
            + "_" + constants.ElasticsearchConstants['index'][schema])

def manage_mapping(index):
    if index == constants.ElasticsearchConstants["index"]["demographics"]:
        return schema.profile_mapping
    elif index == constants.ElasticsearchConstants["index"]["health"]:
        return schema.health_mapping
    elif index == constants.ElasticsearchConstants["index"]["household"]:
        return schema.household_mapping
    elif index == constants.ElasticsearchConstants["index"]["symptoms"]:
        return schema.symptoms_mapping

def _set_demographics(country):
    index = constants.ElasticsearchConstants['index']["demographics"]
    all_mappings = manage_mapping(index)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'
    index = _set_index(country, index)

    if es.indices.exists(index):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = index, body = body )
            logger.info(res)

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)

def _set_household(country):
    index = constants.ElasticsearchConstants["index"]["household"]
    all_mappings = manage_mapping(index)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'
    index = _set_index(country, index)

    if es.indices.exists(index):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = index, body = body )
            logger.info(res)

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)

def _set_health(country):
    index = constants.ElasticsearchConstants["index"]["health"]
    all_mappings = manage_mapping(index)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'
    index = _set_index(country, index)

    if es.indices.exists(index):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = index, body = body )
            logger.info(res)

            if res["acknowledged"] != True:
                logger.info("Index creation failed")
            else:
                logger.info("Index created")

        except ConnectionError as err:
            logger.error(err)

def _set_symptoms(country):
    index = constants.ElasticsearchConstants["index"]["symptoms"]
    all_mappings = manage_mapping(index)

    body = '{ "mappings": ' + json.dumps(all_mappings) + ' }'
    index = _set_index(country, index)

    if es.indices.exists(index):
        logger.debug("INDEX exists")
    else:
        try: 
            res = es.indices.create(index = index, body = body )
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