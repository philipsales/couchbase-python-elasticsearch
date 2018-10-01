import sys
from schemas.mapping_conf import demographics_map
from schemas.mapping_conf import household_map
from schemas.mapping_conf import health_map
from schemas.mapping_conf import symptoms_map
from schemas.mapping_conf import fam_planning_maternal_map
from schemas.mapping_conf import child_health_map
from schemas.mapping_conf import dental_health_map

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
    "mapping_format": demographics_map.demographics,
    "source": "couchbase",
    "destination": "elasticsearch"
}

household = {
    "json_structure": ["cb_id", "organization", "households"],
    "mapping_format": household_map.household,
    "source": "couchbase",
    "destination": "elasticsearch"
}

health = {
    "json_structure": ["cb_id", "organization", "health_informations"],
    "mapping_format": health_map.health,
    "source": "couchbase",
    "destination": "elasticsearch"
}

symptoms = {
    "json_structure": ["cb_id", "organization", "symptoms_collection"],
    "mapping_format": symptoms_map.symptoms,
    "source": "couchbase",
    "destination": "elasticsearch"
}

child_health = {
    "json_structure": ["cb_id", "organization", "child_healths"],
    "mapping_format": child_health_map.child_health,
    "source": "couchbase",
    "destination": "elasticsearch"
}

family_planning_maternal_health = {
    "json_structure": ["cb_id", "organization", "family_planning_and_maternal_healths"],
    "mapping_format": fam_planning_maternal_map.family_planning_and_maternal_health,
    "source": "couchbase",
    "destination": "elasticsearch"
}

dental_health = {
    "json_structure": ["cb_id", "organization", "dental_health"],
    "mapping_format": dental_health_map.dental_health,
    "source": "couchbase",
    "destination": "elasticsearch"
}