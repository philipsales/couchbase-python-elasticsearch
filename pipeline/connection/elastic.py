import sys 
import uuid
import json
import logging

from schemas.output_conf import demographics, health, household, symptoms

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError 

import logs.logging_conf, logging
logger = logging.getLogger("elasticsearch.connection")
import logs.logger as lg

from settings.base_conf import LOGGER_CONSTANTS, ELASTICSEARCH_CONSTANTS
from settings.base_conf import elastic_config

conn = elastic_config.ElasticSearchConfig[elastic_config.ElasticSearchENV]

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

_log_file_name = LOGGER_CONSTANTS['filenames']['etl']

def update_latest(docs, country):
    try:
        for doc in docs:
            try:
                _type = list(doc.keys())
                _body = list(doc.values())

                index = _set_index(country,_type[0])

                es.update(index=index,
                        doc_type=_type[0],
                        id=_body[0]["awh_id"],
                        body={"doc": _body[0]})
            except TypeError:
                print("NoneType object!")
                continue

    except (ConnectionError) as err: 
        logger.error(error)

def _set_json_dump(docs, country):
    create_mappings(country)
    counter = 0
    bulk_data = []

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
    _total_entries(counter)
    bulk_dump(bulk_data, country)
    

def bulk_dump(bulk_data,country):
    try:
        es.bulk(bulk_data)  
    except (ConnectionError) as err: 
        logger.error(error)
    except ValueError as e:
        logger.error(e)
        sys.exit(1)

def batch_dump(docs, country):
        create_mappings(country)
        counter = 0

        try:
            for doc in docs:
                _type = list(doc.keys())
                _body = list(doc.values())

                res = es.index(index = INDEX, 
                         doc_type = _type[0] , 
                         id = _body[0]["awh_id"], 
                         body = _body[0])
                counter += 1

            _total_entries(counter)
            _refresh_index(INDEX)

        except (ConnectionError) as err: 
            logger.error(error)

def _refresh_index(data):
    return es.indices.refresh(index=data)

def _total_entries(count):
    lg.write_to_log("Total Batch Entries: " + str(count) + "\n", _log_file_name)
    print("Total Batch Entries: {%}", count)

def create_mappings(country):
    # Crate mapping for demographics
    _set_mappings(country, ELASTICSEARCH_CONSTANTS['index']["demographics"])
    # Crate mapping for household
    _set_mappings(country, ELASTICSEARCH_CONSTANTS['index']["household"])
    # Crate mapping for health
    _set_mappings(country, ELASTICSEARCH_CONSTANTS["index"]["health"])
    # Crate mapping for symptoms
    _set_mappings(country, ELASTICSEARCH_CONSTANTS["index"]["symptoms"])

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
    return (ELASTICSEARCH_CONSTANTS['country'][country] 
            + "_" + ELASTICSEARCH_CONSTANTS['index'][schema])

def manage_mapping(index):
    if index == ELASTICSEARCH_CONSTANTS["index"]["demographics"]:
        return demographics.profile_mapping
    elif index == ELASTICSEARCH_CONSTANTS["index"]["health"]:
        return health.health_mapping
    elif index == ELASTICSEARCH_CONSTANTS["index"]["household"]:
        return household.household_mapping
    elif index == ELASTICSEARCH_CONSTANTS["index"]["symptoms"]:
        return symptoms.symptoms_mapping

#run as standalone module
if __name__ == "__main__":
    bulk_dump(data)