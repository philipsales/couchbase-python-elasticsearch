import json
import traceback
from pipeline.auxiliary import function_map

import logs.logging_conf, logging
logger = logging.getLogger("mapper")

"""
	CONVERT_TO_FLAT function
	description: Flattens the input json
		Input:
		{
			name: "Rosette Tienzo",
			address: {
				country: "Philippines",
				province: "Pampanga"
			}
		}
		
		Output -> 
		{
			name: "Rosette Tienzo",
			address.country: "Philippines",
			address.province: "Pampanga"
		}

	@ parameters:
		obj - json object to be flatten

	Note: This is made for /schemas/mapping/mappers/* under "key_from"
"""
def convert_to_flat(obj):
	container = {}
	for key, value in obj.items():
		if(type(value).__name__ == "dict"):
			temp = convert_to_flat(value)
			just_in_case = {}
			for key1, value in temp.items():
				key2 = key+"."+key1
				just_in_case[key2] = value 

			container.update(just_in_case)
			continue

		container[key] = value
	
	return container

"""
	MERGER function
	description: Sometimes there are json that are varying with the keys.
					This function will zip it with the default json structure

	@ parameters:
		default - This is the default json structure to which outsider will be zipped with.
					This parameter has the secondary values when outsider values does not exist
		outsider - This is the json that is extracted from the input json.
					This parameter has the primary values for the output
"""
def merger(default, outsider):
	container={}
	for default_key, default_value in default.items():
		flag = False
		for outsider_key, outsider_value in outsider.items():
			if(default_key == outsider_key):
				if(type(outsider_value).__name__ == "dict"):
					container[default_key] = merger(default[default_key], outsider[outsider_key])
				else:
					container[default_key] = outsider_value

				flag = True
		
		if(flag == False):
			container[default_key] = default_value
	
	return container

"""
	DEPT_CREATOR function
	description: If the dept does not exist, this function will create the mother dept then
					append the leaf key and value
	
	@ parameters
		mapper_json - mapping created to map easily from input to output
						refer to /schemas/mapping/mappers/* to further understand
		extracted_json - json extracted from the input
"""
def dept_creator(mapper_json, extracted_json):
	container = {}
	
	arr = mapper_json["parent_key_name"].split(".")
	mother = {}
	for i in range(len(arr)):
		if(i == 0):
			container[arr[i]] = {}
			mother = container[arr[i]]
		else:
			newMother = mother[arr[i]] = {}
			mother = newMother

		if(i == (len(arr)-1)):
			try:
				mother[mapper_json["key_to"]] = extracted_json[mapper_json["key_from"]]
			except KeyError:
				mother[mapper_json["key_to"]] = mapper_json["default_value"]
			
	return container

"""
	DEPT_FINDER function
	description: If the dept already exist, this function will find the mother dept 
					from the final_container then append the leaf key and value
	
	@ parameters
		mapper_json - mapping created to map easily from input to output
						refer to /schemas/mapping/mappers/* to further understand
		final_container - final_container from where the final mapped json should be
		extracted_json - json extracted from the input
"""
def dept_finder(mapper_json, final_container, extracted_json):
	arr = mapper_json["parent_key_name"].split(".")
	mother = {}
	for i in range(len(arr)):
		if(i == 0):
			try:
				mother = final_container[arr[i]]
			except KeyError:
				return False
		else:
			try:
				newMother = mother[arr[i]]
				mother = newMother
			except KeyError:
				newMother = mother[arr[i]] = {}
				mother = newMother

		if(i == (len(arr)-1)):
			try:
				mother[mapper_json["key_to"]] = extracted_json[mapper_json["key_from"]]
			except KeyError:
				mother[mapper_json["key_to"]] = mapper_json["default_value"]

	return final_container

"""
	TRANSFORMER function
	description: Creates the mapping using the mapping_format provided

	@ parameters
		extracted_json - json extracted from the input
		mapping_format - mapping created to map easily from input to output
						refer to /schemas/mapping/mappers/* to further understand
		final_container - final_container from where the final mapped json should be
"""
def transformer(extracted_json, mapping_format, final_container):
	for arr_element in mapping_format:
		if(arr_element["parent_key_name"] == ""):
			if(arr_element["key_from"] != ""):
				if(arr_element["to_compute"]==True):
					final_container[arr_element["key_to"]] = _computations(arr_element["key_to"], extracted_json, arr_element["fields_for_computation"])
				else:
					final_container[arr_element["key_to"]] = extracted_json[arr_element["key_from"]]
			else:
				final_container[arr_element["key_to"]] = arr_element["default_value"]

		elif(arr_element["parent_key_name"] != ""):
			var = dept_finder(arr_element,final_container,extracted_json)
			if(var == False):
				final_container.update(dept_creator(arr_element,extracted_json))
			else:
				final_container.update(var)

	return final_container

'''
	COMPUTATIONS function
	description: This function is responsible for computations
	params:
		_to_compute = which of the computations is to be done. Check out
					/auxiliary/function_map under EXTERNAL FUNCTIONS for
					reference
		
		extracted_json = json extracted from the source
		fields_needed = array of fields needed for the computation. Checkout 
						/schemas/mapping/mappers/* under "fields_for_computation"
						to further understand
'''
def _computations(_to_compute, extracted_json, fields_needed):
	json_attribute = _extract_values(fields_needed, extracted_json)
	result = function_map._execute_computation(json_attribute, _to_compute)
	
	return result

'''
	EXTRACT_VALUES function
	description: The values needed for computations is to be extracted
	params:
		fields_needed = array of fields needed for the computation. Checkout 
						/schemas/mapping/mappers/* under "fields_for_computation"
						to further understand
		extracted_json = json extracted from the source
'''
def _extract_values(fields_needed, extracted_json):
	obj = {}

	for attr in fields_needed:
		obj[attr] = extracted_json[attr]

	return obj