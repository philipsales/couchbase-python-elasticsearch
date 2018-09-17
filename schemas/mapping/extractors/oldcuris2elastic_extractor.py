import sys
from schemas.mapping_conf import oldcuris_elastic_map

'''

json_structure - the json attributes that are to be extracted from the source json
mapping_format - see oldcuris_elastic_map for an example. import it here
input_format - default input of source json
final_format - final input structure. with other fields other than input format
source - source database
destination - destination database

'''

demographics = {
    "json_structure": ["cb_id", "gender", "birthdate","organization","address","profiles"],
    "mapping_format": oldcuris_elastic_map.demographics,
    "source": "couchbase",
    "destination": "elasticsearch"
}

household = {
    "json_structure": ["cb_id", "organization", "households"],
    "mapping_format": oldcuris_elastic_map.household,
    "source": "couchbase",
    "destination": "elasticsearch"
}

health = {
    "json_structure": ["cb_id", "organization", "health_informations"],
    "mapping_format": oldcuris_elastic_map.health,
    "source": "couchbase",
    "destination": "elasticsearch"
}

symptoms = {
    "json_structure": ["cb_id", "organization", "symptoms_collection"],
    "mapping_format": oldcuris_elastic_map.symptoms,
    "source": "couchbase",
    "destination": "elasticsearch"
}