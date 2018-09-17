import settings.couchbase_conf as couchbase_config
import settings.elastic_conf as elastic_config
import settings.kobo_conf as kobo_config
import settings.sqlite_conf as sqlite_conf

COUCHBASE = {
    'philippines': 'Philippines',
    'cambodia': 'Cambodia'
}

ELASTICSEARCH = {
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

LOGGER = {
    'filenames': {
        'etl': 'etl',
        'kobo': 'kobo'
    }
}