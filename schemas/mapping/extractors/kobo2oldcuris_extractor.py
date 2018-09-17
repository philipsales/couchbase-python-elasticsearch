import sys
from schemas.mapping_conf import kobo_oldcuris_map
from schemas.input_conf import personal_info

'''

json_structure - the json attributes that are to be extracted from the source json
mapping_format - see oldcuris_elastic_map for an example. import it here
input_format - default input of source json
final_format - final input structure. with other fields other than input format
source - source database
destination - destination database

'''

personal_informations = {
    "json_structure": [],
    "mapping_format": kobo_oldcuris_map.old_curis_v1,
    "source": "kobo",
    "destination": "couchbase"
}