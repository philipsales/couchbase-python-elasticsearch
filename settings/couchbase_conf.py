
#SERVER Configuration
CouchbaseENV = "development"

CouchbaseConfig = {
    'local': {
        'BUCKET': 'awhcurisdb_dev',
        'USERNAME': '',
        'PASSWORD': '',
        'SCHEME': 'couchbase',
        'IP': '127.0.0.1',
        'HOST': 'couchbase://127.0.0.1/',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'development': {
        'BUCKET': 'awhcurisdb010832',
        'USERNAME': '',
        'PASSWORD': '',
        'SCHEME': 'couchbase',
        'IP': '172.104.49.91',
        'HOST': 'couchbase://172.104.49.91/',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'uat': {
        'BUCKET': 'awhcurisdb',
        'USERNAME': '',
        'PASSWORD': '',
        'SCHEME': 'couchbase',
        'IP': '139.162.18.54',
        'HOST': 'couchbase://139.162.18.54/',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'production': {
        'BUCKET': 'awhcurisdb',
        'USERNAME': '',
        'PASSWORD': '',
        'SCHEME': 'couchbase',
        'IP': '13.76.6.56',
        'HOST': 'couchbase://13.76.6.56/',
        'PORT': '',
        'TIMEOUT': 7200
    }
}

