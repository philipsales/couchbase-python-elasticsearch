import settings.config 

from src.couchBase import CouchbaseConnect
from src.elasticSearch import ElasticsearchConnect
from src.transform import CurisV2ETL 

ENV = 'prod'

cb = settings.config.CouchbaseConfig[ENV]

CB_CONNECTION = cb 
CB_BUCKET = cb['BUCKET']
CB_HOST = cb['HOST'] + cb['BUCKET']

cb = CouchbaseConnect(CB_CONNECTION)
cb_data = cb.n1ql_all()

panda = CurisV2ETL()
es_data = panda.map_address(cb_data)

es = settings.config.ElasticSearchConfig[ENV]
ES_CONNECTION = es 
ES_INDEX = es['INDEX']
ES_DOCTYPE = es['TYPE']

es = ElasticsearchConnect(ES_CONNECTION, ES_INDEX, ES_DOCTYPE)
es.set_mappings()
es.bulk_dump(es_data)
es.get_total()
