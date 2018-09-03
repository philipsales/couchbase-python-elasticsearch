import settings.couchbase_conf as couchbase_config
import settings.elastic_conf as elastic_config
import settings.kobo_conf as kobo_config

COUCHBASE_CONSTANTS = {
    'philippines': 'Philippines',
    'cambodia': 'Cambodia'
}

ELASTICSEARCH_CONSTANTS = {
    'index': {
        'demographics': 'demographics',
        'health': 'health',
        'household': 'household',
        'symptoms': 'symptoms'
    },
    'country': {
        'philippines': 'philippines',
        'cambodia': 'cambodia'
    }
}

LOGGER_CONSTANTS = {
    'filenames': {
        'etl': 'etl',
        'kobo': 'kobo'
    }
}