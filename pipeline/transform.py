import os 
import sys

from pipeline.schemas import profiles
from pipeline.schemas import health
from pipeline.schemas import household
from pipeline.schemas import symptoms

root  = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root +'/logs')

import json

from collections import namedtuple

import logging_conf, logging

logger = logging.getLogger("transformer")

class CurisV2ETL:

    def __init__(self):
        pass

    def pipeline(self,data):
        #TODO insert all pipeline here
        return data

    def map_profile(self, data):
        els_data = []
        profile = {}

        profile = profiles.Profiles(data)
        els_data = profile.map_extracted()
        
        return els_data

    def map_household(self, data):
        els_data = []
        households = {}

        households = household.Household(data)
        els_data = households.map_extracted()

        return household

    def map_health(self, data):
        els_data = []
        healths = {}

        healths = health.Health(data)
        els_data = healths.map_extracted()
        
        return els_data

    def map_symptoms(self, data):
        els_data = []
        symptom = {}

        symptom = symptoms.Symptoms(data)
        els_data = symptom.map_extracted()

        return symptoms

    def map_address(self, documents):
        #TODO map json to object
        counter = 0
        els_data = []

        if not documents:
            raise TypeError("no value")
        else:
            for doc in documents:
                x = self._json2obj(str(doc))

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
               
            return els_data

    def compute_birthdate(self, datas):
        pass

    def _json2obj(self, data): 
        return json.loads(data, object_hook = self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename = True)(*d.values())