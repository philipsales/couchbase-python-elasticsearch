import sys 

CouchbaseConfig = {
    'local': {
        'BUCKET': 'awhcurisdb_dev',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'dev': {
        'BUCKET': 'awhcurisdb010832',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': 'couchbase://172.104.49.91/',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'uat': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'prod': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    }
}

ElasticSearchConfig = {
    'dev': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'local': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'prod': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    }
}





