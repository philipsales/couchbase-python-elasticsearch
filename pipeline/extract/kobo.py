import json
import os 
import sys
import requests
import datetime as dt
import dateutil.parser
import shutil

from requests.exceptions import ConnectionError, RequestException 
from settings.base_conf import LOGGER
from settings.base_conf import kobo_config

import lib.logs.logging_conf, logging
logger = logging.getLogger("kobo.py")
import lib.logs.logger as etl_log

from lib.utility.file_handler import FileHandler

kobo_conn = kobo_config.KoboConfig[kobo_config.KoboENV]

URL = kobo_conn['HOST']
IP_ADDRESS = kobo_conn['IP'] 
TIMEOUT = kobo_conn['TIMEOUT']
PROTOCOL = kobo_conn['PROTOCOL']
PORT = kobo_conn['PORT']
VERSION = kobo_conn['VERSION']
API_ENDPOINT = "data"
PK = kobo_conn['FORM']
USERNAME = kobo_conn['USERNAME']
PASSWORD = kobo_conn['PASSWORD']

_log_file_name = LOGGER['filenames']['kobo']

def kobo_get():

    try:
        sync_date = etl_log.get_last_batch_log(_log_file_name)

        if(sync_date == None):
            raise FileNotFoundError

        _parsed_date = dateutil.parser.parse(sync_date)
        _iso_format_date = dt.datetime.isoformat(_parsed_date)
        logger.info('batch process')
        url = _conn_url(query=_set_query(type='batch', time=_iso_format_date))

    except FileNotFoundError:
        logger.info('initial process')
        url = _conn_url(query=_set_query(type='initial'))

    return _get_data(url)

def _get_data(url):
    #TODO: chokepoint, optimize to any 
    #1. Batch processing
    #2. Parallel 
    #3. Streaming
    try:
        etl_log.write_to_log("\n", _log_file_name)
        etl_log.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        etl_log.write_to_log("url: " + url + "; ", _log_file_name)

        r = requests.get(url, auth=(USERNAME, PASSWORD))
        logger.info('statusCode :' + str(r.status_code))
        logger.info('elapsedTime: ' + str(r.elapsed.total_seconds()))

    except (ConnectionError, RequestException) as err:
        sys.exit(1)

    return r.json()

def kobo_get_stream():

    try:
        sync_date = etl_log.get_last_batch_log(_log_file_name)

        if(sync_date == None):
            raise FileNotFoundError

        _parsed_date = dateutil.parser.parse(sync_date)
        _iso_format_date = dt.datetime.isoformat(_parsed_date)
        logger.info('batch process')

        url = _conn_url(query=_set_query(type='batch', time=_iso_format_date))

    except FileNotFoundError:
        logger.info('initial process')
        url = _conn_url(query=_set_query(type='initial'))

    return _get_data_stream(url)

def _get_data_stream(url):
    try:
        #etl_log.write_to_log("\n", _log_file_name)
        #etl_log.write_to_log("<" + str(dt.datetime.utcnow()) + "> : ", _log_file_name)
        #etl_log.write_to_log("url: " + url + "; ", _log_file_name)

        #TODO: dynamic file path
        local_filename = "data/tmp/" + 'kobo_shutil' + '.json'
        r = requests.get(url, auth=(USERNAME, PASSWORD), stream=True)

        #with open(local_filename, 'wb') as f:
        #TODO: error if file already exist. won't overwrite
        with open(local_filename, 'ab') as f:
            logger.info(str(f))
            shutil.copyfileobj(r.raw, f)

        logger.info('statusCode :' + str(r.status_code))
        logger.info('elapsedTime: ' + str(r.elapsed.total_seconds()))

    except (ConnectionError, RequestException) as err:
        sys.exit(1)

    return True

def _set_query(**kwargs):
    time = kwargs.get('time','')
    batch_type = kwargs.get('type', '')

    if batch_type=='initial':
        query = "query={}"
    elif batch_type=='batch':
        query = ("query={\"_submission_time\": {\"$gt\": \""
            + time + "\"}}")

    logger.info('query: ' + query)
    return query
    
def _conn_url(**kwargs):
    protocol = PROTOCOL
    host = URL
    version = VERSION
    api_endpoint = API_ENDPOINT
    pk = PK
    query = kwargs.get('query', '') 

    urls = protocol + "://"  + host + "/api/" + version + "/" + api_endpoint  + "/" + pk + "?" + query
    logger.info('koboUrl: ' + urls)
    return urls
    