import sys
from schemas.input import old_curis_schema
from schemas.mapping import elastic_schema_map

demographics = {
    "json_structure": ["cb_id", "gender", "birthdate","organization","address","profiles"],
    "mapping_format": elastic_schema_map.demographics,
    "input_format": old_curis_schema.profile
}

household = {
    "json_structure": ["cb_id", "organization", "households"],
    "mapping_format": elastic_schema_map.household,
    "input_format": old_curis_schema.household
}

health = {
    "json_structure": ["cb_id", "organization", "health_informations"],
    "mapping_format": elastic_schema_map.health,
    "input_format": old_curis_schema.health
}

symptoms = {
    "json_structure": ["cb_id", "organization", "symptoms_collection"],
    "mapping_format": elastic_schema_map.symptoms,
    "input_format": old_curis_schema.symptoms
}