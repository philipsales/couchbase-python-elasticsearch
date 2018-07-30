import os 
import sys

import json

from collections import namedtuple

import logs.logging_conf, logging
logger = logging.getLogger("transformer")

"""
data = [
'{"_sync": {"history": {"channels": [null, null, null, null, null], "parents": [4, 0, 1, 2, -1], "revs": ["2-636a886e078abffcb7ae6f26ed4e3145", "3-8fe2be8cf1eb37e5c526fe0b1d8679df", "4-44dbaecccac5e0a63a37991c27fba7e4", "5-3cea7bdc3cf4aff1e55fd443fe385c73", "1-ad48b86cc579666fb3d573d4b298b598"]}, "recent_sequences": [388], "rev": "5-3cea7bdc3cf4aff1e55fd443fe385c73", "sequence": 388, "time_saved": "2018-06-22T14:32:43.70548122Z"}, "address": {"barangay": "Tuburan", "country": "Philippines", "lot_or_house_number": "", "postal_code": "5008", "province": "Iloilo"}, "birthdate": "03/13/1985", "cb_id": "00892236-dded-44f4-ba4a-e7a32931c1e8", "contact_number": {"country_code": "+63", "number": ""}, "email_address": "", "family_members": ["00892236-dded-44f4-ba4a-e7a32931c1e8", "413cabb4-faa6-447f-b2b8-2029598404eb"], "first_name": "Eduardo", "gender": "Male", "health_informations": [], "households": [], "last_name": "Dela Pe\u00f1a", "last_name_suffix": "Jr.", "middle_name": "", "nhid": null, "organization": "Pototan RHU", "profile_picture": {"name": "b5c534bb-e4be-4b5f-b29e-4b223110769c", "path": "/data/data/com.awh.health.curis/app_images/images_resident"}, "profiles": [], "registered_at": "03/05/2018 at 02:56:41 AM GMT+00:00", "type": "user-resident", "user-cam": {"id": "mho.pototan@gmail.com", "owner": "mho.pototan@gmail.com"}}',
'{"_sync": {"history": {"channels": [null, null, null, null, null], "parents": [4, 0, 1, 2, -1], "revs": ["2-636a886e078abffcb7ae6f26ed4e3145", "3-8fe2be8cf1eb37e5c526fe0b1d8679df", "4-44dbaecccac5e0a63a37991c27fba7e4", "5-3cea7bdc3cf4aff1e55fd443fe385c73", "1-ad48b86cc579666fb3d573d4b298b598"]}, "recent_sequences": [388], "rev": "5-3cea7bdc3cf4aff1e55fd443fe385c73", "sequence": 388, "time_saved": "2018-06-22T14:32:43.70548122Z"}, "address": {"barangay": "Tuburan", "country": "Philippines", "lot_or_house_number": "", "postal_code": "5008", "province": "Iloilo"}, "birthdate": "03/13/1985", "cb_id": "00892236-dded-44f4-ba4a-e7a32931c1e8", "contact_number": {"country_code": "+63", "number": ""}, "email_address": "", "family_members": ["00892236-dded-44f4-ba4a-e7a32931c1e8","413cabb4-faa6-447f-b2b8-2029598404eb"], "first_name": "Eduardo", "gender": "Male", "health_informations": [], "households": [], "last_name": "Dela Pe\u00f1a", "last_name_suffix": "Jr.", "middle_name": "", "nhid": null, "organization": "Pototan RHU", "profile_picture": {"name": "b5c534bb-e4be-4b5f-b29e-4b223110769c", "path": "/data/data/com.awh.health.curis/app_images/images_resident"}, "profiles": [], "registered_at": "03/05/2018 at 02:56:41 AM GMT+00:00", "type": "user-resident", "user-cam": {"id": "mho.pototan@gmail.com", "owner": "mho.pototan@gmail.com"}}'
]
"""

def init_pipeline(data, **kwargs):
    #TODO insert all pipeline here
    
    data = map_address(data)
    logger.info(data)
    return data

def map_address(documents):
    #TODO map json to object
    counter = 0
    els_data = []

    if not documents:
        raise TypeError("no value")
    else:
        for doc in documents:
            x = _json2obj(str(doc))

            try:
                address = {
                    "address" : {
                        "community" : x.address.barangay,
                        "province": x.address.province,
                        "zip" : x.address.postal_code 
                        }
                }

            except AttributeError: 
                address = {
                    "address" : {
                        "community" : "",
                        "province": "" ,
                        "zip" : ""
                        }
                }

            els_data.append(json.dumps(address))
            counter += 1
            
        logger.info(els_data)
        return els_data

def _json2obj(data): 
    return json.loads(data, object_hook = _json_object_hook)

def _json_object_hook(d):
    return namedtuple("X", d.keys(), rename = True)(*d.values())

#run as standalone module
if __name__ == "__main__":
    init_pipeline(data)
