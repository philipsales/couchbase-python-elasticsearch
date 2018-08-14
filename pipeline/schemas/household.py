import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.household")

from schemas.input import old_curis_schema
from schemas.mapping import elastic_schema_map
from pipeline import mapper

class Household:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the household section on each json in Curis
    # TODO: Create a template for single json for the array of self.extracted
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
                latestHousehold = old_curis_schema.household

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
            obj = {}

            try:
                # obj = self.map_es_household(household)
                final_obj = mapper.transformer(household,elastic_schema_map.household,obj)
            except AttributeError:
                print("Something went terribly wrong...")
                traceback.print_exc()
                continue

            self.final.append(json.dumps(final_obj))
        
        return self.final

    def map_household(self, data, counter):
        household = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copy the latest household from curis json
                household = data[counter-1].copy()
                # Flatten household for the transformer (look at /schemas/mapping/elastic_schema_map under key_from)
                final_household = mapper.convert_to_flat(household)

        except AttributeError:
            final_household = mapper.convert_to_flat(old_curis_schema.household)

        return final_household
