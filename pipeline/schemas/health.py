import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.health")
from schemas.input import old_curis_schema
from pipeline import mapper
from schemas.mapping import elastic_schema_map

class Health:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    # Extracts the health informations section on each json in Curis
    # TODO: Create a template for single json for the array of self.extracted
    def extract_health(self):
        for i in self.arr:
            # Converts JSON object to Python object
            x = json.loads(i)
            
            try:
                # Destructuring the mother json
                (cb_id, health_informations, organization) = (x["cb_id"], x["health_informations"], x["organization"])
                
                #Gets latest counter of the array of health informations
                ctr:int = len(health_informations)

                # Assigning to a variable the extracted latest health information
                lastestHealthInfo = self.map_health_informations(health_informations, ctr)

                # Initializing the doc to be sent
                obj = {
                    "cb_id" : cb_id,
                    "organization": organization
                }

                # Updating the obj with the health informations JSON fields
                obj.update(lastestHealthInfo)

            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue
                
            except KeyError:
                (cb_id, organization) = (x["cb_id"], x["organization"])
                lastestHealthInfo = mapper.convert_to_flat(old_curis_schema.health)

                obj = {
                    "cb_id": cb_id,
                    "organization": organization
                }

                obj.update(lastestHealthInfo)
            #push to a global variable the extracted one
            self.extracted.append(json.dumps(obj))

        return self.extracted
    
    #Map From extracted JSON to Elasticsearch schema
    def map_extracted(self):
        # Extract from Curis JSON first
        self.extract_health()
        counter = 0

        # Start mapping to Elasticsearch schema
        for x in self.extracted:
            
            # Convert JSON object to Python object
            health = json.loads(x)
            obj = {}

            try:
                # Mapping starts here
                final_obj = mapper.transformer(health,elastic_schema_map.health,obj)

            # Happens when there is a missing attribute in the 'health' object
            except AttributeError:
                logger.info("Something went terribly wrong!")
                traceback.print_exc()
                continue

            self.final.append(json.dumps(final_obj))
            counter += 1
            print('--transform: ', counter)
        
        return self.final

    # Mapping to health informations structure from Curis JSON
    def map_health_informations(self, data, ctr):
        healthInformations = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copy the latest health_informations from curis json
                curis_json = data[ctr-1].copy()
                # Fold default json with the copied latest health_informations
                healthInformations = mapper.merger(old_curis_schema.health, curis_json)
                # Compute BMI and add to json to be passed to the mapper
                healthInformations["bmi"] = self.computeBodyMassIndex(healthInformations["height"], healthInformations["weight"])
                # Flatten health_health informations for the transformer  (look at /schemas/mapping/elastic_schema_map under key_from)
                final_health = mapper.convert_to_flat(healthInformations)

        except AttributeError:
            # Passing the object structure of Curis object under health_informations into the variable
            final_health = mapper.convert_to_flat(old_curis_schema.health)
        
        return final_health
    
    # Compute body mass weight
    def computeBodyMassIndex(self, height, weight):
        bmi_result = ""

        try:
            try:
                # Convert height and weight to integer
                height = int(height)
                weight = int(weight)

            # If values are empty strings...
            except ValueError:
                height = 0
                weight = 0

            # If height is less than 10, the height is probably not in metric
            if height <= 10.0:
                # So.. we convert it to metric (inch)
                height = height * .3048
                
            # Computation of BMI happens here
            bmi = weight / (height * height)

            # Assigning the BMI result here
            if bmi <= 18.5:
                bmi_result = "Underweight"
            elif 18.6 <= bmi <= 24.9:
                bmi_result = "Normal"
            elif 25 <= bmi <= 29.9:
                bmi_result = "Overweight"
            elif bmi >= 30:
                bmi_result = "Obese"
        # This happens when height and weight is a string
        except TypeError:
            bmi_result = ""
        
        # This happens when the values are zeros
        except ZeroDivisionError:
            bmi_result = ""
        
        return bmi_result
