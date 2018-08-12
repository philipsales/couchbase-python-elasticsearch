import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.household")

import mappings.default_receiver

class Household:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the household section on each json in Curis
    def extract_household(self):
        for i in self.arr:
            x = json.loads(i)

            try:
                (cb_id, households, organization) = (x["cb_id"], x["households"],x["organization"])
                ctr:int = len(households)

                #Initialize object to be push in extracted array
                obj = {
                    "cb_id": cb_id,
                    "organization": organization
                }

                latestHousehold = self.map_household(households, ctr)

                obj.update(latestHousehold)
            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue

            except KeyError:
                (cb_id, organization) = (x["cb_id"], x["organization"])
                latestHousehold = mappings.default_receiver.household

                obj = {
                    "cb_id": cb_id,
                    "organization": organization
                }

                obj.update(latestHousehold)

            self.extracted.append(json.dumps(obj))

        return self.extracted
    
    #Map to Elasticsearch schema
    def map_extracted(self):
        self.extract_household()
        for x in self.extracted:
            household = json.loads(x)

            try:
                obj = self.map_es_household(household)
            except AttributeError:
                print("Something went terribly wrong...")
                traceback.print_exc()
                continue

            self.final.append(json.dumps(obj))
        
        return self.final

    def map_household(self, data, counter):
        household = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                household = data[counter-1].copy()

        except AttributeError:
            household = mappings.default_receiver.household

        return household

    def map_es_household(self, household):
        obj = {
            "awh_id": household["cb_id"],
            "families_in_household": household["no_of_families_in_the_household"],
            "people_in_household": household["no_of_people_in_the_household"],
            "type_of_accommodation": household["house_ownership"],
            "construction": household["type_of_house"],
            "type_of_neighbourhood": household["neighborhood_description"],
            "utilities": household["amenities_present_in_house"], 
            "type_of_sanitation": household["sanitary_type"], 
            "sanitation_ownerships": household["sanitary_ownership"],
            "org": household["organization"],
            "version":{
                "number": 1,
                "date": datetime.datetime.now().isoformat()
            }
        }

        return obj