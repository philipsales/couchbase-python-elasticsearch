import settings.config 

from lib.couchBase import SyncGatewayConnect, N1QLConnect
from lib.elasticSearch import ElasticsearchConnect
from lib.transform import CurisV2ETL 

cb_ENV = 'dev'
es_ENV = 'local'

cb = settings.config.CouchbaseConfig[cb_ENV]
es = settings.config.ElasticSearchConfig[es_ENV]

CB_CONNECTION = cb 
cbs = SyncGatewayConnect(CB_CONNECTION)
cbs_data = cbs.get_all()

>>>>>>> feature-logs.01
cb = N1QLConnect(CB_CONNECTION)
cb_data = cb.get_all()

etl = CurisV2ETL()
es_data = etl.map_address(cb_data)

ES_CONNECTION = es 
es = ElasticsearchConnect(ES_CONNECTION)
es.bulk_dump(es_data)
