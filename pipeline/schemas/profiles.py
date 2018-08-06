import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.profiles")

import mappings.curis_schema
from pipeline import mapper

class Profiles:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the profiles section on each json in Curis
    def extract_profiles(self):
        logger.info(mappings.curis_schema)
        for j in self.arr:
            # Convert JSON to Python object
            x = json.loads(j)

            try:
                # Destructure json extracted from Curis
                (cb_id, gender, year_of_birth, address) = (x["cb_id"],x["gender"], x["birthdate"], x["address"])
                (profile, organization) = (x["profiles"], x["organization"])

                # Get the length of the profile array
                ctr:int = len(profile)
                
                # Initialize the JSON to be push as profiles in self.extracted
                obj = {
                    "cb_id": cb_id,
                    "gender":gender,
                    "year_of_birth":year_of_birth,
                    "organization":organization
                }

                #Map address to the expected fields in the mapping on elasticsearch schema
                address1 = mapper.mapper(address)
                #Map profile to the expected fields in the mapping on elasticsearch schema
                profile1 = self.map_profiles(profile, ctr)

                #Add the json attributes of address and profile in the initial json object
                obj.update(address1)
                obj.update(profile1)

                #Append to self.extracted json
                self.extracted.append(json.dumps(obj))

            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue
            
        return self.extracted
    
    # Map to elasticsearch schema
    def map_extracted(self):
        #Calling self.extract_profiles() here to extract from Curis array first
        self.extract_profiles()
        counter = 0
        # For loop for mapping into elasticsearch schema
        for x in self.extracted:
            # Convert JSON object to Python object first
            person = json.loads(x)

            try:
                # Map the address and employment from Extracted JSON to Elasticsearch Schema
                address = self.map_address(person)
                employment = self.map_employment(person)

                # Mapping to elasticsearch schema starts here
                obj = self.map_es_profiles(person, address, employment)

            # Happens when there is a missing attribute in 'person' object
            except AttributeError:
                logger.info("Something went terribly wrong!")
                traceback.print_exc()
                continue

            # Appending to final array
            # json.dumps converts the object from Python object to JSON string object
            self.final.append(json.dumps(obj))
            counter += 1
            print('--transform: ', counter)

        return self.final
    
    # Maps address attribute to the expected elasticsearch schema object structure
    def map_address(self, data):
        address = {}
        try:
            address = {
                "add_date": datetime.datetime.now().isoformat(),
                "commnty": data["barangay"],
                "province": data["province"]
            }

        except AttributeError:
            address = {
                "add_date": None,
                "commnty": "",
                "province": ""
            }

        return address
    
    # Maps employment attribute to the expected elasticsearch schema object structure
    def map_employment(self, data):
        employment = {}

        try:
            employment = {
                "is_empl": data["is_employed"],
                "m_income": data["monthly_income"],
                "nature": data["nature"]
            }

        except AttributeError:
            employment = {
                "is_empl": "",
                "m_income": 0.0,
                "nature": ""
            }
        except KeyError:
            employment = {
                "is_empl": "",
                "m_income": 0.0,
                "nature": ""
            }

        return employment

    # Extracting latest profiles attribute from Curis JSON
    def map_profiles(self, data, ctr):
        finalProfiles = {}
        counter = ctr-1

        try: 
            if(len(data) == 0):
                raise AttributeError
            elif(len(data) > 0):
                finalProfiles = mapper.mapper(data[counter])

        except AttributeError:
            # Assigning the template of the profile attribute to the variable
            finalProfiles = mappings.curis_schema.profile
            traceback.print_exc()

        return finalProfiles

    def map_es_profiles(self, person, address, employment):
        obj = {
            "awh_id": person["cb_id"],
            "active": True,
            "sex": person["gender"],
            "birth_date": person["year_of_birth"],
            "deceased": {
                "is_dead": False,
                "year": None,
            },
            "address": address,
            "org": person["organization"],
            "civil_st": person["civil_status"],
            "religion": person["religion"],
            "educ": person["education"],
            "employed": employment,
            "version": {
                "number": 1,
                "date": datetime.datetime.now().isoformat()
            }
        }

        return obj

    def _json2obj(self, data): 
        return json.loads(data, object_hook = self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename = True)(*d.values())