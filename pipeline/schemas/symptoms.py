import sys
import json
import datetime
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.symptoms")

import mappings.default_receiver

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the symptoms section on each json in Curis
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
                latestSymptoms = mappings.default_receiver.symptoms

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

            try:
                # Mapping the extracted json to the elasticsearch schema
                head = self.map_head(symptoms["head"])
                arms = self.map_arms(symptoms["arms"])
                chest = self.map_chest(symptoms["chest"])
                legs = self.map_legs(symptoms["legs"])
                pelvis = self.map_pelvis(symptoms["pelvis"])
                neck = self.map_neck(symptoms["neck"])

                obj = {
                    "awh_id": symptoms["cb_id"],
                    "head": head,
                    "neck": neck,
                    "chest": chest,
                    "arms": arms,
                    "abdomen": symptoms["abdomen"]["abdomen"],
                    "pelvis": pelvis,
                    "legs": legs,
                    "skin": symptoms["skin"]["skin"],
                    "org": symptoms["organization"],
                    "version":{
                        "number": 1,
                        "date": datetime.datetime.now().isoformat()
                    }
                }

                self.final.append(json.dumps(obj))
            
            except:
                print("Something went terribly wrong!!!")
                traceback.print_exc()
                continue
            
        return self.final

    """
    INTERNAL FUNCTIONS
    """

    #Function for mapping head
    def map_head(self, datum):
        #Creating an object to be passed
        try:
            head = {
                "head": datum["head"],
                "eyes": datum["eyes"],
                "nose": datum["nose"],
                "mouth": datum["mouth"],
                "chin_jaw": datum["chin_and_jaw"],
                "ears": datum["ears"]
            }
        
        except AttributeError:
            head = {
                "head": [],
                "eyes": [],
                "nose": [],
                "mouth": [],
                "chin_jaw": [],
                "ears": []
            }

        return head

    #Function for mapping neck
    def map_neck(self, datum):
        #Creating an object to be passed
        try:
            neck = {
                "neck": datum["neck"],
                "throat": datum["throat"],
                "upperback": datum["upperback"],
                "lowerback": datum["lowerback"],
                "shoulder": datum["shoulders"]
            }
        
        except AttributeError:
            neck = {
                "neck": [],
                "throat": [],
                "upperback": [],
                "lowerback": [],
                "shoulder": []
            }

        return neck

    #Function for mapping chest
    def map_chest(self, datum):
        #Creating an object to be passed
        try:
            chest = {
                "chest": datum["chest"],
                "lungs": datum["lungs_and_breathing"]
            }
        except AttributeError:
            chest = {
                "chest": [],
                "lungs": []
            }

        return chest

    #Function for mapping arms
    def map_arms(self, datum):
        #Creating an object to be passed
        try:
            arms = {
                "upper": datum["upper_arm"],
                "elbow": datum["elbow"],
                "lower": datum["lower_arm"],
                "wrist": datum["wrist"],
                "hand": datum["hand_and_palm"],
                "fingers": datum["fingers"]
            }
        except AttributeError:
            arms = {
                "upper": [],
                "elbow": [],
                "lower": [],
                "wrist": [],
                "hand": [],
                "fingers": []
            }

        return arms

    #Function for mapping pelvis
    def map_pelvis(self, datum):
        #Creating an object to be passed
        try:
            pelvis = {
                "hip": datum["hip"],
                "pelvis": datum["pelvis"],
                "genitals": datum["genitals"]
            }
        except AttributeError:
            pelvis = {
                "hip": [],
                "pelvis": [],
                "genitals": []
            }

        return pelvis

    #Function for mapping legs
    def map_legs(self, datum):
        #Creating an object to be passed
        try:
            legs = {
                "thigh": datum["thigh"],
                "shin": datum["shin"],
                "knee": datum["knee"],
                "foot": datum["foot"],
                "toes": datum["toes"]
            }
        except AttributeError:
            legs = {
                "thigh": [],
                "shin": [],
                "knee": [],
                "foot": [],
                "toes": []
            }

        return legs
    
    def map_symptoms(self, data, ctr):
        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                finalSymptoms = data[ctr-1].copy()

        except AttributeError:
            finalSymptoms = mappings.default_receiver.symptoms
        
        return finalSymptoms