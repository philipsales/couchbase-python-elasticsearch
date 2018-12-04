import sys

from settings.base_conf import OLDCURIS_CHILD_HEALTH_CSV_MAP
from settings.base_conf import OLDCURIS_DEMOGRAPHICS_CSV_MAP
from settings.base_conf import OLDCURIS_HOUSEHOLD_CSV_MAP
from settings.base_conf import OLDCURIS_HEALTH_CSV_MAP
from settings.base_conf import OLDCURIS_FAMILY_HEALTH_CSV_MAP
from settings.base_conf import OLDCURIS_DENTAL_HEALTH_CSV_MAP
from settings.base_conf import OLDCURIS_SYMPTOMS_CSV_MAP
from settings.base_conf import OLDCURIS_RISK_SCORE_CSV_MAP


'''

json_structure - the json attributes that are to be extracted from the source json
mapping_format - see oldcuris_elastic_map for an example. import it here
input_format - default input of source json
final_format - final input structure. with other fields other than input format
source - source database
destination - destination database

'''

demographics = {
    "json_structure": ["cb_id", "gender", "birthdate","organization","address","profiles","user-cam"],
    "mapping_file": OLDCURIS_DEMOGRAPHICS_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

household = {
    "json_structure": ["cb_id", "organization", "households","user-cam"],
    "mapping_file": OLDCURIS_HOUSEHOLD_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

health = {
    "json_structure": ["cb_id", "organization", "health_informations","user-cam"],
    "mapping_file": OLDCURIS_HEALTH_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

symptoms = {
    "json_structure": ["cb_id", "organization", "symptoms_collection","user-cam"],
    "mapping_file": OLDCURIS_SYMPTOMS_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

child_health = {
    "json_structure": ["cb_id", "organization", "child_healths","user-cam"],
    "mapping_file": OLDCURIS_CHILD_HEALTH_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

family_planning_maternal_health = {
    "json_structure": ["cb_id", "organization", "family_planning_and_maternal_healths","user-cam"],
    "mapping_file": OLDCURIS_FAMILY_HEALTH_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

dental_health = {
    "json_structure": ["cb_id", "organization", "dental_health","user-cam"],
    "mapping_file": OLDCURIS_DENTAL_HEALTH_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}

risk_score = {
    "json_structure": ["cb_id", "organization", "profiles","households","identification","user-cam"],
    "mapping_file": OLDCURIS_RISK_SCORE_CSV_MAP,
    "source": "couchbase",
    "destination": "elasticsearch"
}