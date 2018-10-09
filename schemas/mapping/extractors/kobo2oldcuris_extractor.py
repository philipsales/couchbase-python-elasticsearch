import sys
from schemas.input_conf import personal_info

from settings.base_conf import KOBO_PERSONAL_INFO_CSV_MAP

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
    "mapping_file": KOBO_PERSONAL_INFO_CSV_MAP,
    "source": "kobo",
    "destination": "couchbase"
}