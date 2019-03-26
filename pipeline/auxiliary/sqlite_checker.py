import json
from pipeline.connection import sqlite
from pipeline.connection import couchbase_n1ql

import logs.settings.logging_conf, logging
logger = logging.getLogger("auxiliary.sqlite_checker")

def segregate_ids(conn,data):
    new_ids = []
    old_ids = []

    for datum in data:
        user = sqlite.get_one_data(conn, datum['kobo_id'])
        if(user == None):
            sqlite.insert_data(conn, datum['kobo_id'])
            new_ids.append(datum)
        else:
            old_ids.append(datum)

    sqlite.close_db(conn)
    
    result = {
        "new_data": new_ids, 
        "old_data": old_ids
    }

    return result

def update_many_kobo(conn, raw_data, cb_response):
    for idx, datum in enumerate(raw_data):
        sqlite.update_data(conn, cb_response[idx], datum["kobo_id"])

def update_one_kobo(conn, raw_data, cb_response):
    raw_data = json.loads(raw_data)
    sqlite.update_data(conn, cb_response, raw_data['kobo_id'])

def get_id(conn, kobo_id):
    user = sqlite.get_one_data(conn, kobo_id)
    return user

def update_rev_ids(conn):
    sqlite_ids = sqlite.get_many_data(conn)
    cb_ids = _get_cb_ids(sqlite_ids)
    rev_ids = couchbase_n1ql.get_rev_ids(cb_ids)

    data_arr = _organize_data(sqlite_ids, rev_ids)
    logger.info("Updating rev ids...")
    update_many_kobo(conn, data_arr, data_arr)

def _organize_data(sqlite_data, rev_ids):
    tmp_arr = []
    tmp_json = {}

    if(rev_ids != []):
        for idx, datum in enumerate(sqlite_data):
            one_rev = json.loads(rev_ids[idx])
        
            tmp_json["id"] = datum[0]
            tmp_json["rev"] = one_rev["rev_id"]
            tmp_json["kobo_id"] = datum[1]

            tmp_arr.extend([tmp_json])
    else:
        tmp_arr = []

    return tmp_arr

def _get_cb_ids(sqlite_data):
    tmp_arr = []
    for datum in sqlite_data:
        tmp_arr.extend([datum[0]])

    return tmp_arr