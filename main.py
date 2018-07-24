import settings.config 

from src.couchBase import SyncGatewayConnect
from src.couchBase import N1QLConnect
from src.elasticSearch import ElasticsearchConnect
from src.transform import CurisV2ETL 

ENV = 'prod'

cb = settings.config.CouchbaseConfig[ENV]
es = settings.config.ElasticSearchConfig[ENV]

CB_CONNECTION = cb 
cb = N1QLConnect(CB_CONNECTION)
cb_data = cb.get_all()

etl = CurisV2ETL()
es_data = etl.pipeline(cb_data)

ES_CONNECTION = es 
es = ElasticsearchConnect(ES_CONNECTION)
es.bulk_dump(es_data)
