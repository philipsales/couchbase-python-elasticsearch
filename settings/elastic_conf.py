
ElasticSearchENV = "local"

ElasticSearchConfig = {
    'local': {
        'USERNAME': 'elastic',
        'PASSWORD': 'elastic',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'development': {
        'USERNAME': 'kibanaadmin',
        'PASSWORD': 'AWH@dm1n',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'https',
        'HOST': '172.104.184.192',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'production': {
        'USERNAME': 'elastic',
        'PASSWORD': 'elastic',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    }
}





