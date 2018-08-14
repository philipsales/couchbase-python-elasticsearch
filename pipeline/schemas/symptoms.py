import sys
import json
import datetime
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.symptoms")

from schemas.input import old_curis_schema
from pipeline import mapper
from schemas.mapping import elastic_schema_map

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the symptoms section on each json in Curis
    # TODO: Create a template for single json for the array of self.extracted
    def extract_symptoms(self):
        for i in self.arr:
            # Convert JSON object to Python object
            # x = self._json2obj(str(i))
            x = json.loads(i)

            try:
                # Destructuring Curis json
                (symptoms, cb_id, organization) = (x["symptoms_collection"], x["cb_id"], x["organization"])
                ctr:int = len(symptoms)

                # Initialize the object to be appended in self.extracted
                obj = {
                    "cb_id": cb_id,
                    "organization": organization
                }

                # Gets latest symptoms in the array of symptoms
                latestSymptoms = self.map_symptoms(symptoms, ctr)

                # Update the object with the extracted latest symptoms
                obj.update(latestSymptoms)
            
            # Throws this exception when x.symptoms does not exist
            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue

            except KeyError:
                (cb_id, organization) = (x["cb_id"], x["organization"])
                
                latestSymptoms = mapper.convert_to_flat(old_curis_schema.symptoms)

                obj = {
                    "cb_id": cb_id,
                    "organization": organization
                }

                obj.update(latestSymptoms)

            # Push to self.extracted the JSON
            self.extracted.append(json.dumps(obj))

        return self.extracted
    
    #Map to Elasticsearch schema
    def map_extracted(self):
        #Call extract function to get symptoms section in Curis JSON
        self.extract_symptoms()

        #Looping through the extracted array
        for x in self.extracted:
            # symptoms = self._json2obj(str(x))
            symptoms = json.loads(x)
            obj = {}

            try:
                # Mapping the extracted json to the elasticsearch schema
                final_obj = mapper.transformer(symptoms,elastic_schema_map.symptoms,obj)
            
            except:
                print("Something went terribly wrong!!!")
                traceback.print_exc()
                continue
            
            self.final.append(json.dumps(final_obj))
        return self.final
    
    def map_symptoms(self, data, ctr):
        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copy latest symptoms from array of objects from Curis json
                curis_data = data[ctr-1].copy()
                # Fold default json with the copied latest symptoms
                merged = mapper.merger(old_curis_schema.symptoms, curis_data)
                # Flatten symptoms for the transformer (look at /schemas/mapping/elastic_schema_map under key_from)
                finalSymptoms = mapper.convert_to_flat(merged)

        except AttributeError:
            finalSymptoms = mapper.convert_to_flat(old_curis_schema.symptoms)
        
        return finalSymptoms