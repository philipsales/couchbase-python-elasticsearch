
#SERVER Configuration
SQLiteENV = "development"

SQLiteConfig = {
    'development': {
        'PATH': './data/kobosqlite_dev.db',
        'DB_NAME': 'kobosqlite',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': '',
        'SCHEME': 'sqlite',
        'IP': '',
        'HOST': '',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200
    },
    'uat': {
        'PATH': './data/kobosqlite_uat.db',
        'DB_NAME': 'kobosqlite',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': '',
        'SCHEME': 'sqlite',
        'IP': '',
        'HOST': '',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200
    },
    'production': {
        'PATH': './data/kobosqlite_prod.db',
        'DB_NAME': 'kobosqlite',
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': '',
        'SCHEME': 'sqlite',
        'IP': '',
        'HOST': '',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200
    }
}