import json
from pipeline.connection import sqlite

def segregate_ids(conn,data):
    new_ids = []
    old_ids = []

    for datum in data:
        user = sqlite.get_data(conn, datum['kobo_id'])
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
        sqlite.update_data(conn, cb_response[idx]["id"], 
            cb_response[idx]["rev"],
            datum["kobo_id"])

def update_one_kobo(conn, raw_data, cb_response):
    raw_data = json.loads(raw_data)
    sqlite.update_data(conn, cb_response["id"], 
            cb_response["rev"],
            raw_data['kobo_id'])

def get_id(conn, kobo_id):
    user = sqlite.get_data(conn, kobo_id)
    return user