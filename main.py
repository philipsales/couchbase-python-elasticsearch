import os 
import sys

import logs

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV
from settings.constants import CouchbaseConstants

from pipeline.couchbase_syncgateway import SyncGatewayConnect 
from pipeline.couchbase_n1ql import N1QLConnect 
from pipeline.elasticsearch import ElasticsearchConnect 
from pipeline.transform import CurisV2ETL

def main():
    # Initializing Couchbase
    cb_conn = CouchbaseConfig[CouchbaseENV]
    cb_sync = SyncGatewayConnect(cb_conn)
    cb = N1QLConnect(cb_conn)

    # Initializing constants
    cb_constants = CouchbaseConstants

    # Initializing Elasticsearch
    es_conn = ElasticSearchConfig[ElasticSearchENV]
    es = ElasticsearchConnect(es_conn)

    # Initializing ETL
    etl = CurisV2ETL()

    # Cuartero data
    cb_cuartero = cb.get_all(cb_constants['cuartero'])
    es_data_cuartero = etl.map_profile(cb_cuartero)
    es.bulk_dump(es_data_cuartero)

    # Pototan data
    # cb_pototan = cb.get_all(cb_constants['pototan'])
    # es_data_pototan = etl.map_profile(cb_pototan)
    # es.bulk_dump(es_data_pototan)

    # Guimbal data
    # cb_guimbal = cb.get_all(cb_constants['guimbal'])
    # es_data_guimbal = etl.map_profile(cb_guimbal)
    # es.bulk_dump(es_data_guimbal)

if __name__ == '__main__':
    main()
