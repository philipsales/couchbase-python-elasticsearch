import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.health")
import mappings.curis_schema
from pipeline import mapper

class Health:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    # Extracts the health informations section on each json in Curis
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

                #push to a global variable the extracted one
                self.extracted.append(json.dumps(obj))
            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue

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

            try:
                # Map blood pressure to expected object structure in elasticsearch schema
                bloodPressure = self.map_blood_pressure(health["blood_pressure"])
                # Compute body mass index
                bmi = self.computeBodyMassIndex(health["height"], health["weight"])

                # Mapping starts here
                obj = self.map_es_health(health, bmi, bloodPressure)
            
            # Happens when there is a missing attribute in the 'health' object
            except AttributeError:
                logger.info("Something went terribly wrong!")
                traceback.print_exc()
                continue

            self.final.append(json.dumps(obj))
            counter += 1
            print('--transform: ', counter)
        
        return self.final

    def map_blood_pressure(self, data):
        
        try:
            # Mapping to the object structure of blood pressure in elasticsearch schema
            bloodPressure = {
                "first": {
                    "systole": data.first_reading.systole,
                    "diastole": data.first_reading.diastole
                },
                "second": {
                    "systole": data.second_reading.systole,
                    "diastole": data.second_reading.diastole
                },
                "third": {
                    "systole": data.third_reading.systole,
                    "diastole": data.third_reading.diastole
                }
            }
        except AttributeError:
            # Creating an empty object structure of blood pressure in elasticsearch schema
            bloodPressure = {
                "first": {
                    "systole": 0.0,
                    "diastole": 0.0
                },
                "second": {
                    "systole": 0.0,
                    "diastole": 0.0
                },
                "third": {
                    "systole": 0.0,
                    "diastole": 0.0
                }
            }

        return bloodPressure
    # Mapping to health informations structure from Curis JSON
    def map_health_informations(self, data, ctr):

        healthInformations = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copy the data from the json data[ctr-1] to healthInformations
                healthInformations = data[ctr-1].copy()

        except AttributeError:
            # Passing the object structure of Curis object under health_informations into the variable
            healthInformations = mappings.curis_schema.health
            
        
        return healthInformations
    
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

    def map_es_health(self, health, bmi, bloodPressure):
        try:
            obj = {
                "awh_id": health["cb_id"],
                "bmi": bmi,
                "blood_group": health["blood_type"],
                "blood_rhesus": health["blood_sign"],
                "allergies": health["allergies"],
                "bp": bloodPressure,
                "blood_sugar": health["blood_sugar"],
                "smoking_habit": health["smoking_habit"],
                "fruits_in_a_week": health["fruits_in_a_week"],
                "vegetables_in_a_week": health["vegetables_in_a_week"],
                "exercise_in_a_week": health["exercise_in_a_week"],
                "family_history": health["family_history"],
                "diagnosed": health["diagnosed"],
                "medical_equipments": health["medical_equipments"],
                "maintenance_drugs": health["maintenance_drugs"],
                "org": health["organization"],
                "version":{
                    "number": 1,
                    "date": datetime.datetime.now().isoformat()
                }
            }
        except KeyError:
            obj = {
                "awh_id": health["cb_id"],
                "bmi": bmi,
                "blood_group": health["blood_type"],
                "blood_rhesus": health["blood_sign"],
                "allergies": health["allergies"],
                "bp": bloodPressure,
                "blood_sugar": health["blood_sugar"],
                "smoking_habit": health["smoking_habit"],
                "fruits_in_a_week": health["fruits_in_a_week"],
                "vegetables_in_a_week": health["vegetables_in_a_week"],
                "exercise_in_a_week": health["exercise_in_a_week"],
                "family_history": health["family_history"],
                "diagnosed": health["diagnosed"],
                "high_cost_medicine": health["high_cost_medicine"],
                "maintenance_drugs": health["maintenance_drugs"],
                "org": health["organization"],
                "version":{
                    "number": 1,
                    "date": datetime.datetime.now().isoformat()
                }
            }

        return obj