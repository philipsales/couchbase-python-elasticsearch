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
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
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
<<<<<<< HEAD
    'dev': {
=======
    'local': {
>>>>>>> feature-logs.01
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
<<<<<<< HEAD
    'local': {
=======
    'dev': {
>>>>>>> feature-logs.01
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





