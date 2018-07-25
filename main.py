import os 
import sys

root  = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root +'/lib')

from settings.couchbase_conf import CouchbaseConfig, CouchbaseENV
from settings.elastic_conf import ElasticSearchConfig, ElasticSearchENV 

from pipeline.couchbase_syncgateway import SyncGatewayConnect 
from pipeline.couchbase_n1ql import N1QLConnect 
from pipeline.elasticsearch import ElasticsearchConnect 
from pipeline.transform import CurisV2ETL

cb_conn = CouchbaseConfig[CouchbaseENV]
cb = SyncGatewayConnect(cb_conn)
cb_data = cb.get_all()

cb = N1QLConnect(cb_conn)
cb_data = cb.get_all()

etl = CurisV2ETL()
es_data = etl.map_address(cb_data)

es_conn = ElasticSearchConfig[ElasticSearchENV]
es = ElasticsearchConnect(es_conn)
es.bulk_dump(es_data)
