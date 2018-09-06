import sys
import json
import traceback

from pipeline.transformation import mapper

import logs.logging_conf, logging
logger = logging.getLogger("extractor")
    
def extract_from_input(arr, extract_settings):

    extracted = []

    for j in arr:
        try:
            x = json.loads(j)

            obj = _deconstruct(x, extract_settings)
            extracted.append(json.dumps(obj))
        except TypeError:
            obj = _deconstruct(j, extract_settings)
            extracted.append(json.dumps(obj))
    
    return extracted

def _deconstruct(data, extract_settings):
    json_obj = {}
    
    if len(extract_settings["json_structure"]) != 0:
        for json_attribute in extract_settings["json_structure"]:
            try:
                if(type(data[json_attribute]).__name__ == "list"):
                    ctr = len(data[json_attribute])
                    if(ctr==0):
                        json_obj[json_attribute] = extract_settings["input_format"]
                    else:
                        json_obj[json_attribute] = get_latest(data[json_attribute], ctr)
                else:
                    json_obj[json_attribute] = data[json_attribute]

            except KeyError:
                json_obj[json_attribute] = extract_settings["input_format"]

    elif len(extract_settings["json_structure"]) == 0:
        json_obj = data

    final_json_obj = mapper.merger(extract_settings["final_format"], json_obj)
    
    _flat_json = mapper.convert_to_flat(final_json_obj)
    return _flat_json

def map_to_output(raw_data, extract_settings):
    final = []
    extracted = extract_from_input(raw_data, extract_settings)
    counter = 0

    for x in extracted:
        _json_object = json.loads(x)
        obj = {}

        try:
            final_obj = mapper.transformer(_json_object,extract_settings["mapping_format"],obj)
        except AttributeError:
            logger.info("Something went terribly wrong!")
            traceback.print_exc()
            continue

        final_obj = _json_format(extract_settings["destination"],final_obj)
        final.append(final_obj)
        counter += 1
        logger.info('--transform: ' + str(counter))

    return final

def get_latest(datum, counter):
    obj = datum[counter-1].copy()
    return obj

def _json_format(destination, obj):
    if(destination=="couchbase"):
        return obj
    else:
        return json.dumps(obj)