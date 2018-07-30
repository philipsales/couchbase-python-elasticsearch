import sys
import json
import datetime
from collections import namedtuple
import traceback

import mappings.curis_schema

class Symptoms:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the symptoms section on each json in Curis
    def extract_symptoms(self):
        for i in self.arr:
            # Convert JSON object to Python object
            x = self._json2obj(str(i))

            try:
                # Destructuring Curis json
                (symptoms, cb_id) = (x.symptoms,x.cb_id)
                ctr:int = len(symptoms)
                
                # Initialize the object to be appended in self.extracted
                obj = {
                    "cb_id":cb_id
                }

                # Gets latest symptoms in the array of symptoms
                latestSymptoms = self.map_symptoms(symptoms, ctr)

                # Update the object with the extracted latest symptoms
                obj.update(latestSymptoms)

                # Push to self.extracted the JSON
                self.extracted.append(json.dumps(obj))
            
            # Throws this exception when x.symptoms does not exist
            except AttributeError:
                print("Something went wrong...")
                continue

        return self.extracted
    
    #Map to Elasticsearch schema
    def map_extracted(self):
        #Call extract function to get symptoms section in Curis JSON
        self.extract_symptoms()

        #Looping through the extracted array
        for x in self.extracted:
            symptoms = self._json2obj(str(x))

            try:
                # Mapping the extracted json to the elasticsearch schema
                head = self.map_head(symptoms)
                arms = self.map_arms(symptoms)
                chest = self.map_chest(symptoms)
                legs = self.map_legs(symptoms)
                pelvis = self.map_pelvis(symptoms)
                neck = self.map_neck(symptoms)

                obj = {
                    "awh_id": symptoms.cb_id,
                    "head": head,
                    "neck": neck,
                    "chest": chest,
                    "arms": arms,
                    "abdomen": symptoms["abdomen"]["abdomen"],
                    "pelvis": pelvis,
                    "legs": legs,
                    "skin": symptoms["skin"]["skin"],
                    "version":{
                        "number": 1,
                        "date": datetime.datetime.now()
                    }
                }

                self.final.append(json.dumps(obj))
            
            except:
                pass
            
        return self.final

    """
    INTERNAL FUNCTIONS
    """

    #Function for mapping head
    def map_head(self, datum):
        #Creating an object to be passed
        try:
            head = {
                "head": datum.head,
                "eyes": datum.eyes,
                "nose": datum.nose,
                "mouth": datum.mouth,
                "chin_jaw": datum.chin_and_jaw,
                "ears": datum.ears
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
                "neck": datum.neck,
                "throat": datum.throat,
                "upperback": datum.upperback,
                "lowerback": datum.lowerback,
                "shoulder": datum.shoulder
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

        return leg
    
    def map_symptoms(self, data, ctr):
        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                finalSymptoms = data[ctr-1].copy

        except AttributeError:
            finalSymptoms = mappings.curis_schema.symptoms
        
        return finalSymptoms

    def _json2obj(self, data): 
        return json.loads(data, object_hook = self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename = True)(*d.values())