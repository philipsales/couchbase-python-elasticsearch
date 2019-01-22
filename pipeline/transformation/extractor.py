import sys
import json
import traceback

from pipeline.transformation import mapper
from pipeline.cleaning import cleaner

from pipeline.transformation import converter

from settings.base_conf import DATA_TYPE

import logs.logging_conf, logging
logger = logging.getLogger("extractor")

COUCHBASE = "couchbase"

def extract_from_input(raw_data, extract_settings, input_schema):
    extracted = []

    for j in raw_data:
        try:
            x = json.loads(j)

            obj = _deconstruct(x, extract_settings, input_schema)
            extracted.append(json.dumps(obj))
        except TypeError:
            obj = _deconstruct(j, extract_settings, input_schema)
            extracted.append(json.dumps(obj))
    
    return extracted

def transform(extracted, extract_settings, output_schema):
    final = []
    counter = 0

    for x in extracted:
        _json_object = json.loads(x)
        obj = {}

        try:
            mapping_format = converter.csv2json(extract_settings['mapping_file'])

            final_obj = mapper.transformer(_json_object, mapping_format, obj)
        except AttributeError:
            logger.info("Something went terribly wrong!")
            traceback.print_exc()
            continue

        final_obj = _datatype_checker(output_schema, final_obj)

        final_obj = _json_format(extract_settings["destination"], final_obj)
        final.append(final_obj)
        counter += 1

        logger.info('transform: ' + str(counter))

    return final

def _deconstruct(data, extract_settings, input_schema):
    json_obj = {}
    
    if len(extract_settings["json_structure"]) != 0:
        for json_attribute in extract_settings["json_structure"]:
            try:
                if(type(data[json_attribute]).__name__ == "list"):
                    ctr = len(data[json_attribute])
                    if(ctr==0):
                        json_obj[json_attribute] = _get_key_and_values(
                                    input_schema[json_attribute]['default'])
                    else:
                        json_obj[json_attribute] = _get_latest(data[json_attribute], ctr)
                else:
                    json_obj[json_attribute] = data[json_attribute]

            except KeyError:
                json_obj[json_attribute] = _get_key_and_values(input_schema[json_attribute]['default'])

    elif len(extract_settings["json_structure"]) == 0:
        json_obj = data

    final_json_obj = mapper.merger(input_schema, json_obj)
    # final_json_obj = cleaner.clean_data(final_json_obj)

    _flat_json = mapper.convert_to_flat(final_json_obj)
    
    return _flat_json

def _get_latest(datum, counter):
    obj = datum[counter-1].copy()
    return obj

def _json_format(destination, obj):
    if(destination==COUCHBASE):
        return obj
    else:
        return json.dumps(obj)

def _datatype_checker(output_schema, final_obj):
    for key, value in final_obj.items():
        try:
            schema_datatype = type(output_schema[key]['default']).__name__
            obj_datatype = type(value).__name__

            if(schema_datatype == obj_datatype):
                if(output_schema[key]['type'] == DATA_TYPE['object']):
                    _datatype_checker(output_schema[key]['default'], value)
                elif(output_schema[key]['type'] == DATA_TYPE['array']):
                    tmp_array = []

                    if(type(value).__name__ == 'list'):
                        tmp_array.extend(value)
                    else:
                        tmp_array.extend([value])

                    final_obj[key] = tmp_array
                else:
                    continue
            else:
                if((str(schema_datatype) == 'dict') or (str(schema_datatype) == 'list')):
                    continue
                else:
                    final_obj[key] = _type_casting(output_schema[key]['default'], value)
                    

        except KeyError:
            logger.warn(str(key) + " does not exist on the output schema")

    return final_obj

def _type_casting(default_value, final_value):
    #Check typecasting if value is NULL, '', or 0
    try:
       final_value =  type(default_value)(final_value)
    except (TypeError, ValueError) as e:
        logger.warn("not compatible: " + str(e))
    except KeyError as e:
        logger.err("key does not exist")

    return final_value

def _get_key_and_values(json_obj):
    final_json = {}
    for key, value in json_obj.items():
        if(type(value['default']).__name__ == "dict"):
            final_json[key] = _get_key_and_values(value['default'])
        else:
            final_json[key] = value['default']

    return final_json