import sys
import datetime
import json
from collections import namedtuple
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.profiles")

import mappings.curis_schema

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
            x = self._json2obj(str(j))

            try:
                # Destructure json extracted from Curis
                (cb_id,gender, year_of_birth, address) = (x.cb_id,x.gender, x.birthdate, x.address)
                (profile, organization) = (x.profiles, x.organization)

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
                address = self.map_address(address)
                #Map profile to the expected fields in the mapping on elasticsearch schema
                profile = self.map_profiles(profile, ctr)

                #Add the json attributes of address and profile in the initial json object
                obj.update(address)
                obj.update(profile)

                #Append to self.extracted json
                self.extracted.append(json.dumps(obj))

            except AttributeError:
                #Do something if AttributeError is raised
                #IF THERE'S ANYTHING TO DO
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue
            
        return self.extracted

    # def clean_data(self):
    #     self.extract_profiles()
    #     profiles = pipe.Pipeline(self.extracted)
    #     hello = profiles.changeToTitleCase()
        
    #     return hi
    
    # Map to elasticsearch schema
    def map_extracted(self):
        #Calling self.extract_profiles() here to extract from Curis array first
        self.extract_profiles()
        counter = 0
        # For loop for mapping into elasticsearch schema
        for x in self.extracted:
            # Convert JSON object to Python object first
            person = self._json2obj(str(x))

            try:
                # Map the address and employment from Extracted JSON to Elasticsearch Schema
                address = self.map_address(person)
                employment = self.map_employment(person)

                # Mapping to elasticsearch schema starts here
                obj = {
                    "awh_id": person.cb_id,
                    "active": True,
                    "sex": person.gender,
                    "yr_birth": person.year_of_birth,
                    "deceased": {
                        "is_dead": False,
                        "year": None,
                    },
                    "address": address,
                    "org": person.organization,
                    "civil_st": person.civil_status,
                    "religion": person.religion,
                    "educ": person.education,
                    "employed": employment,
                    "version": {
                        "number": 1,
                        "date": datetime.datetime.now().isoformat()
                    }
                }
            
            # Happens when there is a missing attribute in 'person' object
            except AttributeError:
                #Do something if AttributeError is raised
                #IF THERE'S ANYTHING TO DO
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
                "commnty": data.barangay,
                "province": data.province
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
                "is_empl": data.is_employed,
                "m_income": data.monthly_income,
                "nature": data.nature
            }

        except AttributeError:
            employment = {
                "is_empl": "",
                "m_income": 0.0,
                "nature": ""
            }

        return employment

    # Extracting latest profiles attribute from Curis JSON
    def map_profiles(self, data, ctr):
        finalProfiles = {}

        try: 
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copying the latest profile in the Curis JSON to the variable
                finalProfiles = data[ctr-1].copy()

        except AttributeError:
            # Assigning the template of the profile attribute to the variable
            finalProfiles = mappings.curis_schema.profile

        return finalProfiles

    def _json2obj(self, data): 
        return json.loads(data, object_hook = self._json_object_hook)

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys(), rename = True)(*d.values())