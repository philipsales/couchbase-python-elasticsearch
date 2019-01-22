import json
import os 
import sys
import requests
import datetime as dt

from couchbase.bucket import Bucket
from couchbase.n1ql import N1QLQuery, N1QLError
from couchbase.exceptions import CouchbaseTransientError
from couchbase.exceptions import CouchbaseNetworkError
from requests.exceptions import ConnectionError, RequestException 

import logs.logger as lg

from settings.base_conf import LOGGER, COUCHBASE
from settings.base_conf import couchbase_config

import logs.logging_conf, logging
logger = logging.getLogger("couchbase.n1q1")

conn = couchbase_config.CouchbaseConfig[couchbase_config.CouchbaseENV]

BUCKET = conn['BUCKET'] 
URL = conn['HOST'] + conn['BUCKET']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
API_ENDPOINT = "_all_docs?"

_log_file_name = LOGGER['filenames']['etl']

def couchbase_get(country):
    try:
        sync_date = lg.get_last_batch_log(_log_file_name)

        if(sync_date == None):
            raise FileNotFoundError

        statement = _set_statement(type='batch',country=country,sync_date=sync_date)

        logger.info(statement)
        
    except FileNotFoundError:
        statement = _set_statement(type='initial',country=country)
        logger.info(statement)

    res = _get_all(statement)
    return _dict2json(res, True)

def get_rev_ids(cb_id_arr):
    statement = ("SELECT _sync.rev as rev_id FROM "
                + BUCKET + " USE KEYS " + str(cb_id_arr))

    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT

        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 

        res = bucket.n1ql_query(query)

    except (RequestException, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.error(err)

    return _dict2json(res, False)

def _get_all(statement): 
    try:
        bucket = Bucket(URL)
        bucket.n1ql_timeout = TIMEOUT

        lg.write_to_log("\n", _log_file_name)
        lg.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        lg.write_to_log("Query: " + statement + "; ", _log_file_name)

        query = N1QLQuery(statement)
        query.timeout = TIMEOUT 

        res = bucket.n1ql_query(query)

    except (RequestException, CouchbaseTransientError, CouchbaseNetworkError) as err: 
        logger.error(err)
        sys.exit(1)

    return res

def _set_statement(**kwargs):
    query_type = kwargs.get('type', "")
    country = kwargs.get('country',"")
    country_iso = country.lower() + "_iso"

    #max =  37,324 
    if query_type=="initial":
        query = ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                    + BUCKET + ".* FROM "
                    + BUCKET + " WHERE (address.country='"
                    + country + "' OR address.country='"
                    + COUCHBASE[country_iso] + "') AND _deleted IS MISSING AND "
                    + "LOWER(organization)!='test rhu' AND "
                    + "type='user-resident'")
    elif query_type=="batch":
        date_sync = kwargs.get('sync_date', "")

        query = ("SELECT meta(" + BUCKET + ").id as cb_id, " 
                    + BUCKET + ".* FROM "
                    + BUCKET + " WHERE (address.country='"
                    + country + "' OR address.country='"
                    + COUCHBASE[country_iso] + "') AND _deleted IS MISSING AND " 
                    + "LOWER(organization)!='test rhu' AND "
                    + "type='user-resident' AND _sync.time_saved LIKE '"
                    + date_sync + "%'")

    return query
    # return ("SELECT meta(" + BUCKET + ").id as cb_id, " 
    #                 + BUCKET + ".* FROM "
    #                 + BUCKET + " WHERE address.country='"
    #                 + country + "' AND _deleted IS MISSING AND "
    #                 + "LOWER(organization)!='test rhu' AND "
    #                 + "type='user-resident' LIMIT 5")

def _dict2json(results, is_etl):
    counter = 0
    data = []

    for row in results: 
        data.append(json.dumps(row))
        counter += 1
        logger.info(counter)

    if(is_etl == True):
        lg.write_to_log("Count From Couchbase: " + str(counter) 
                        + "; ", _log_file_name)

    logger.info("couchbase data size: %s" % str(counter))
    return data

def _set_log_filename(country):
    file_name = ""
    if country == PHILIPPINES:
        file_name = LOG_PHL

    elif country == CAMBODIA:
        file_name = LOG_KHM
    
    return file_name

#run as standalone module
if __name__ == "__main__":
    get_all()