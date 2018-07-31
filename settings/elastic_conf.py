
ElasticSearchENV = "development"

ElasticSearchConfig = {
    'local': {
        'USERNAME': 'elastic',
        'PASSWORD': 'elastic',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 360
    },
    'development': {
        'USERNAME': 'elkadmin',
        'PASSWORD': 'admin(1)n@AWH',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'http',
        'HOST': '172.104.184.192',
        'PORT': 9200,
        'TIMEOUT': 360
    },
    'production': {
        'USERNAME': 'elastic',
        'PASSWORD': 'elastic',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 360
    }
}





