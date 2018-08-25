import sys
import json
import traceback

import logs.logging_conf, logging
logger = logging.getLogger("schema.profiles")

from schemas.input import old_curis_schema
from pipeline import mapper
from schemas.mapping import elastic_schema_map

class Profiles:

    def __init__(self, raw_data):
        self.arr = raw_data
        self.extracted = []
        self.final = []
        
    #Extracts the profiles section on each json in Curis
    # TODO: Create a template for single json for the array of self.extracted
    def extract_profiles(self):
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
                address1 = mapper.convert_to_flat(address)
                #Map profile to the expected fields in the mapping on elasticsearch schema
                profile1 = self.map_profiles(profile, ctr)

                #Add the json attributes of address and profile in the initial json object
                obj.update(address1)
                obj.update(profile1)

            except AttributeError:
                logger.info("Something went wrong...")
                traceback.print_exc()
                continue

            except KeyError:
                (cb_id, gender, year_of_birth, address, organization) = (x["cb_id"],x["gender"], x["birthdate"], x["address"], x["organization"])
                address1 = mapper.convert_to_flat(address)
                profile1 = mapper.convert_to_flat(old_curis_schema.profile)

                obj = {
                    "cb_id": cb_id,
                    "gender":gender,
                    "year_of_birth":year_of_birth,
                    "organization":organization
                }

                obj.update(address1)
                obj.update(profile1)
                
            #Append to self.extracted json
            self.extracted.append(json.dumps(obj))
            
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
            obj = {}

            try:
                # Mapping to elasticsearch schema starts here
                final_obj = mapper.transformer(person,elastic_schema_map.demographics,obj)

            # Happens when there is a missing attribute in 'person' object
            except AttributeError:
                logger.info("Something went terribly wrong!")
                traceback.print_exc()
                continue

            # Appending to final array
            # json.dumps converts the object from Python object to JSON string object
            self.final.append(json.dumps(final_obj))
            counter += 1
            print('--transform: ', counter)

        return self.final

    # Extracting latest profiles attribute from Curis JSON
    def map_profiles(self, data, ctr):
        finalProfiles = {}

        try:
            if(len(data) == 0):
                raise AttributeError
            else:
                # Copy the latest profiles from curis json
                curis_json = data[ctr-1].copy()
                # Flatten profiles for the transformer (look at /schemas/mapping/elastic_schema_map under key_from)
                final_profiles = mapper.convert_to_flat(curis_json)
        except AttributeError:
            # Assigning the template of the profile attribute to the variable
            final_profiles = mapper.convert_to_flat(old_curis_schema.profile)

        return final_profiles
