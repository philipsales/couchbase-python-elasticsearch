import sys
import datetime
import json
from collections import namedtuple
import traceback

import mappings.curis_schema

class Household:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the household section on each json in Curis
    def extract_household(self):
        for i in self.arr:
            x = self._json2obj(str(i))

            try:
                (cb_id, households) = (x.cb_id, x.households)
                ctr:int = len(households)

                #Initialize object to be push in extracted array
                obj = {
                    "cb_id": cb_id
                }

                latestHousehold = self.map_household(households, ctr)

                obj.update(latestHousehold)
            except AttributeError:
                print("Something went wrong...")
                traceback.print_exc()
                continue

            self.extracted.append(json.dumps(obj))

        return self.extracted

    # def clean_data(self):
    #     self.extract_household()
    #     pass
    
    #Map to Elasticsearch schema
    def map_extracted(self):
        self.extract_household()
        for x in self.extracted:
            household = self._json2obj(str(x))

            try:
                obj = {
                    "awh_id": household.cb_id,
                    "families_in_household": household.no_of_families_in_the_household,
                    "people_in_household": household.no_of_people_in_the_household,
                    "type_of_accommodation": household.house_ownership,
                    "construction": household.type_of_house,
                    "type_of_neighbourhood": household.neighborhood_description,
                    "utilities": household.amenities_present_in_house, 
                    "type_of_sanitation": household.sanitary_type, 
                    "sanitation_ownerships": household.sanitary_ownership,
                    "version":{
                        "number": 1,
                        "date": datetime.datetime.now().isoformat()
                    }
                }
            except AttributeError:
                print("Something went terribly wrong...")
                traceback.print_exc()
                continue

            self.final.append(obj)
        
        return self.final

    def map_household(self, data, counter):
        household = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                household = data[counter-1].copy()

        except AttributeError:
            household = mappings.curis_schema.household

        return household



    def _json2obj(self, data): 
        return json.loads(data, object_hook = self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename = True)(*d.values())