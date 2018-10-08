import sys
import json
import csv

DEFAULT_INT = 0
DEFAULT_FLOAT = 0.0
DEFAULT_BOOL = False
DEFAULT_DATE = "date_now"

def csv2json(csv_filename):
    csvfile = open(csv_filename, 'r')

    field_names = ("parent_key_name","key_to","key_from","default_value","fields_for_computation","to_compute","type")

    csv_reader = csv.DictReader(csvfile,field_names)
    header = next(csv_reader)
    line_count = 0
    out = json.dumps( [ row for row in csv_reader ] )

    final_container = _set_json_mapping(out)

    return final_container

def _set_json_mapping(array_obj):
	container = []

	array_obj = json.loads(array_obj)

	for obj in array_obj:
		obj["fields_for_computation"] = _set_field_for_computation(obj["fields_for_computation"])
		obj["to_compute"] = _set_to_compute(obj["to_compute"])
		obj["default_value"] = _set_default_value(obj["type"], obj["default_value"])

		container.extend([obj])

	return container

def _set_field_for_computation(the_value):
	array_string = []
	if(the_value != ""):
		the_value = the_value.replace(" ", "")
		array_string = the_value.split(",")

	return array_string

def _set_to_compute(the_value):
	is_to_compute = False
	if(the_value != ""):
		is_to_compute = True
	
	return is_to_compute

def _set_default_value(data_type, the_value):
	default_val = ""

	if(data_type == "array"):
		if(the_value != ""):
			default_val = the_value
		else:
			default_val = []
	elif(data_type == "boolean"):
		default_val = DEFAULT_BOOL
	elif(data_type == "date"):
		default_val = DEFAULT_DATE
	elif(data_type == "integer"):
		default_val = DEFAULT_INT
	elif(data_type == "string"):
		if(the_value != ""):
			default_val = the_value
	elif(data_type == "float"):
		default_val = DEFAULT_FLOAT

	return default_val