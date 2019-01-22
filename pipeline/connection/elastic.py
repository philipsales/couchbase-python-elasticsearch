import sys 
import uuid
import json
import logging

from schemas.output_conf import demographics
from schemas.output_conf import health
from schemas.output_conf import household
from schemas.output_conf import symptoms
from schemas.output_conf import child_health
from schemas.output_conf import fam_planning_maternal
from schemas.output_conf import dental_health
from schemas.output_conf import risk_score

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError 

import logs.logging_conf, logging
logger = logging.getLogger("elasticsearch.connection")
import logs.logger as lg

from settings.base_conf import LOGGER, ELASTICSEARCH
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
    # scheme = conn['SCHEME'],
    # port = conn['PORT'],
    timeout = int(conn['TIMEOUT']))

_log_file_name = LOGGER['filenames']['etl']

DEMOGRAPHICS = ELASTICSEARCH['index']['demographics']
HOUSEHOLD = ELASTICSEARCH['index']['household']
HEALTH = ELASTICSEARCH['index']['health']
SYMPTOMS = ELASTICSEARCH['index']['symptoms']
CHILD_HEALTH = ELASTICSEARCH['index']['child_health']
FAM_PLAN_MATERNAL = ELASTICSEARCH['index']['family_planning_and_maternal_health']
DENTAL_HEALTH = ELASTICSEARCH['index']['dental_health']
RISK_SCORE = ELASTICSEARCH['index']['risk_score']

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
                logger.error("NoneType object!")
                continue

    except (ConnectionError) as err: 
        logger.error(error)

def set_json_dump(docs, country):
    _create_mappings(country)
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
            logger.info("type: %s, fields: %d" % (_type[0], len(_type[0])))
            counter += 1

        except TypeError:
            logger.error("NoneType object!")
            continue
    logger.info("total index inserts %d" % len(doc))
    
    logger.info(bulk_data)
    _total_entries(counter)
    _bulk_dump(bulk_data, country)
    
def _bulk_dump(bulk_data,country):
    try:
        es.bulk(bulk_data)  
    except (ConnectionError) as err: 
        logger.error(error)
    except ValueError as e:
        logger.error(e)

def _batch_dump(docs, country):
        _create_mappings(country)
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
    lg.write_to_log("Total Batch Entries: " + str(count), _log_file_name)
    print("Total Batch Entries: {%}", count)

def _create_mappings(country):
    _set_mappings(country, DEMOGRAPHICS)
    _set_mappings(country, HOUSEHOLD)
    _set_mappings(country, HEALTH)
    _set_mappings(country, SYMPTOMS)
    _set_mappings(country, CHILD_HEALTH)
    _set_mappings(country, FAM_PLAN_MATERNAL)
    _set_mappings(country, DENTAL_HEALTH)
    _set_mappings(country, RISK_SCORE)

def _set_mappings(country, index):
    all_mappings = _manage_mapping(index)

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
    return (ELASTICSEARCH['country'][country] 
            + "_" + ELASTICSEARCH['index'][schema])

def _manage_mapping(index):
    if index == DEMOGRAPHICS:
        return demographics.profile_mapping
    elif index == HEALTH:
        return health.health_mapping
    elif index == HOUSEHOLD:
        return household.household_mapping
    elif index == SYMPTOMS:
        return symptoms.symptoms_mapping
    elif index == CHILD_HEALTH:
        return child_health.child_health_mapping
    elif index == FAM_PLAN_MATERNAL:
        return fam_planning_maternal.family_planning_mapping
    elif index == DENTAL_HEALTH:
        return dental_health.dental_health_mapping
    elif index == RISK_SCORE:
        return risk_score.risk_score_mapping

def _set_log_filename(country):
    if country == PHILIPPINES:
        return LOG_PHL
    elif country == CAMBODIA:
        return LOG_KHM

def get_data(index):
    _res = {}
    _offsets = 0 
    _limit = 3332
    _index = index 
    _doc_type = ''

    _doc = {
        'size' : _limit,
        'from' : _offsets,
        'query': {
            'match_all' : {}
       }
   }

    try:
        _res = es.search(index=_index, 
                        body=_doc)
        print(_res)
        return _res
    except (ConnectionError) as err: 
        logger.error(error)


#run as standalone module
if __name__ == "__main__":
    bulk_dump(data)