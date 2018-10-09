import settings.couchbase_conf as couchbase_config
import settings.elastic_conf as elastic_config
import settings.kobo_conf as kobo_config
import settings.sqlite_conf as sqlite_conf

from pathlib import Path

KOBO_CSV_MAPPING_PATH = Path("schemas/mapping/csv_mappers/")
OLDCURIS_CSV_MAPPING_PATH = Path("schemas/mapping/csv_mappers/oldcuris2elastic/")

KOBO_PERSONAL_INFO_CSV_MAP = KOBO_CSV_MAPPING_PATH / "kobo2oldcuris_mapping_5_2_2.csv"

OLDCURIS_DEMOGRAPHICS_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "demographics_mapping.csv"
OLDCURIS_HOUSEHOLD_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "household_mapping.csv"
OLDCURIS_HEALTH_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "health_mapping.csv"
OLDCURIS_CHILD_HEALTH_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "child_health_mapping.csv"
OLDCURIS_FAMILY_HEALTH_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "family_planning_maternal_mapping.csv"
OLDCURIS_DENTAL_HEALTH_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "dental_health_mapping.csv"
OLDCURIS_SYMPTOMS_CSV_MAP = OLDCURIS_CSV_MAPPING_PATH / "symptoms_mapping.csv"

COUCHBASE = {
    'philippines': 'Philippines',
    'philippines_iso': 'PHL',
    'cambodia': 'Cambodia',
    'cambodia_iso': 'KHM'
}

ELASTICSEARCH = {
    'index': {
        'demographics': 'demographics',
        'health': 'health',
        'household': 'household',
        'symptoms': 'symptoms',
        'child_health': 'child_health',
        'family_planning_and_maternal_health' : 'family_planning_and_maternal_health',
        'dental_health': 'dental_health'
    },
    'country': {
        'philippines': 'philippines',
        'cambodia': 'cambodia'
    }
}

LOGGER = {
    'filenames': {
        'etl': 'etl',
        'kobo': 'kobo'
    }
}

DATA_TYPE = {
    'array': 'array',
    'string': 'string',
    'date': 'date',
    'integer': 'integer',
    'float': 'float',
    'object': 'object'
}