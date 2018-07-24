import sys
import json
from collections import namedtuple

class CurisV2ETL:

    def __init__(self):
        pass

    def map_address(self, datas):
        counter = 0
        els_data = []

        for data in datas:
            x = self._json2obj(str(data))

            try:
                address = {
                    "address" : {
                        "community" : x.address.barangay,
                        "province": x.address.province ,
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
            print('--transform: ', counter)

        return els_data

    def _json2obj(self, data): 
        return json.loads(data, object_hook=self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename=True)(*d.values())
