import sys
from schemas.mapping import kobo_oldcuris_map
from schemas.input import kobo_schema

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
    "mapping_format": kobo_oldcuris_map.old_curis,
    "input_format": kobo_schema.personal_info,
    "final_format": kobo_schema.personal_info,
    "source": "kobo",
    "destination": "couchbase"
}