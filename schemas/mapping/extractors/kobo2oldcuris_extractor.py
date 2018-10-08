import sys
from schemas.mapping_conf import kobo_oldcuris_map
from schemas.input_conf import personal_info
from pathlib import Path

'''

json_structure - the json attributes that are to be extracted from the source json
mapping_format - see oldcuris_elastic_map for an example. import it here
input_format - default input of source json
final_format - final input structure. with other fields other than input format
source - source database
destination - destination database

'''

CSV_MAPPING_PATH = Path("schemas/mapping/csv_mappers/")
CSV_FILE_PERSONAL_INFO = CSV_MAPPING_PATH / "kobo2oldcuris_mapping_5_2_2.csv"

# CSV_MAPPING_PATH = "../csv_mappers/"
# CSV_FILE_PERSONAL_INFO = "kobo2oldcuris_mapping_5_2_2.csv"

personal_informations = {
    "json_structure": [],
    "mapping_format": kobo_oldcuris_map.old_curis,
    "mapping_file": CSV_FILE_PERSONAL_INFO,
    "source": "kobo",
    "destination": "couchbase"
}