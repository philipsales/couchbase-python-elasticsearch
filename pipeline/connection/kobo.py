import json
import os 
import sys
import requests
import datetime as dt
import dateutil.parser

import logs.logger as lg
import logs.logging_conf, logging
logger = logging.getLogger("kobo")

from settings.base_conf import LOGGER_CONSTANTS
from settings.base_conf import kobo_config

conn = kobo_config.KoboConfig[kobo_config.KoboENV]

URL = conn['HOST']
IP_ADDRESS = conn['IP'] 
TIMEOUT = conn['TIMEOUT']
PROTOCOL = conn['PROTOCOL']
PORT = conn['PORT']
VERSION = conn['VERSION']
API_ENDPOINT = "data"
PK = "5"
USERNAME = conn['USERNAME']
PASSWORD = conn['PASSWORD']

_log_file_name = LOGGER_CONSTANTS['filenames']['kobo']

def _kobo_get():
    try:
        sync_date = lg._get_last_batch_log(_log_file_name)
        _parsed_date = dateutil.parser.parse(sync_date)
        _iso_format_date = dt.datetime.isoformat(_parsed_date)

        url = _conn_url(query=_set_query(type='batch', time=_iso_format_date))

    except FileNotFoundError:
        url = _conn_url(query=_set_query(type='initial'))

    return get_data(url)

def get_data(url):
    try:
        
        lg.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        lg.write_to_log("url: " + url + "; ", _log_file_name)

        r = requests.get(url, auth=(USERNAME, PASSWORD))
        logger.info(r.status_code)
        logger.info(r.elapsed.total_seconds())

    except (ConnectionError, RequestException) as err:
        sys.exit(1)

    return r.json()

def _set_query(**kwargs):

    time = kwargs.get('time','')
    batch_type = kwargs.get('type', '')

    if batch_type=='initial':
        query = "query={}"
    elif batch_type=='batch':
        query = ("query={\"_submission_time\": {\"$gt\": \""
            + time + "\"}}")

    return query
    
def _conn_url(**kwargs):
    protocol = PROTOCOL
    host = URL
    version = VERSION
    api_endpoint = API_ENDPOINT
    pk = PK
    query = kwargs.get('query', '') 

    urls = protocol + "://"  + host + "/api/" + version + "/" + api_endpoint  + "/" + pk + "?" + query
    return urls
    