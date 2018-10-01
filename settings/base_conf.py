import settings.couchbase_conf as couchbase_config
import settings.elastic_conf as elastic_config
import settings.kobo_conf as kobo_config
import settings.sqlite_conf as sqlite_conf

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