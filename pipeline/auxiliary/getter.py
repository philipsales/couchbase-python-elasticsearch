import json
from schemas.input_conf import input_schemas
from schemas.output_conf import output_schemas

OLD_CURIS = 'old_curis'

def get_input_schema(source_project, fields_needed):
    schema = input_schemas[source_project]
    schema_properties = schema['properties']
    
    final_json = _extract_json_structure(schema_properties, fields_needed)
    return final_json

def get_output_schema(source_project, specific_schema):
    schema = output_schemas[source_project][specific_schema]
    schema_properties = schema['properties']
    
    final_json = _extract_json_structure(schema_properties, [])
    return final_json

def _extract_json_structure(schema_properties, fields_needed):
    final_json_struct = {}
    
    if fields_needed != []:
        for field in fields_needed:
            final_json_struct = _classify_datatype(final_json_struct, schema_properties, field)
    else:
        for field in schema_properties:
            final_json_struct = _classify_datatype(final_json_struct, schema_properties, field)
    
    return final_json_struct

def _classify_datatype(final_json_struct, schema_properties, field):
    if(schema_properties[field]['type'] == 'object'):

        try:
            inner_schema = schema_properties[field]['properties']
            final_json_struct[field] = _extract_json_structure(inner_schema, [])
        except KeyError:
            final_json_struct[field] = {}

    elif(schema_properties[field]['type'] == 'array'):

        try:
            inner_schema = schema_properties[field]['items']['properties']
            final_json_struct[field] = _extract_json_structure(inner_schema, [])
        except KeyError:
            final_json_struct[field] = []
            
    else:
        final_json_struct[field] = schema_properties[field]['default']

    return final_json_struct