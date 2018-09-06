import json
from pipeline.connection import sqlite

def segregate_ids(conn,data):
    new_ids = []
    old_ids = []

    for datum in data:
        user = sqlite._get_data(conn, datum['kobo_id'])
        if(user == None):
            sqlite._insert_data(conn, datum['kobo_id'])
            new_ids.append(datum)
        else:
            old_ids.append(datum)

    sqlite._close_db(conn)
    return {"new_data": new_ids, "old_data": old_ids}

def update_kobo(conn, raw_data, cb_response, _type):

    if(_type == "multiple"):
        for idx, datum in enumerate(raw_data):
            sqlite._update_data(conn, cb_response[idx]["id"], 
                cb_response[idx]["rev"],
                datum["kobo_id"])
                
    elif(_type == "single"):
        raw_data = json.loads(raw_data)
        sqlite._update_data(conn, cb_response["id"], 
                cb_response["rev"],
                raw_data['kobo_id'])

def _get_id(conn, kobo_id):
    user = sqlite._get_data(conn, kobo_id)
    return user