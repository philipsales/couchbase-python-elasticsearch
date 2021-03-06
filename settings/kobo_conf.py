
#SERVER Configuration
KoboENV = "production"

KoboConfig = {
    'local': {
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'SCHEME': 'kobo',
        'IP': '127.0.0.1',
        'HOST': '',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200,
        'FORM': ''
    },
    'development': {
        'USERNAME': 'admin',
        'PASSWORD': 'admin',
        'PROTOCOL': 'https',
        'SCHEME': 'kobo',
        'IP': '',
        'HOST': 'kc.aqm.space',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200,
        'FORM': '12'
    },
    'uat': {
        'USERNAME': '',
        'PASSWORD': '',
        'PROTOCOL': 'http',
        'SCHEME': 'kobo',
        'IP': '',
        'HOST': '',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200,
        'FORM': ''
    },
    'production': {
        'USERNAME': 'admin',
        'PASSWORD': 'adm(1)n@AWH',
        'PROTOCOL': 'https',
        'SCHEME': 'kobo',
        'IP': '',
        'HOST': 'kc.aqm.space',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200,
        'FORM': '13'
    }
}
# FORM: 33 for testing 2 set
# FORM: 12 for actual testing
# FROM: 13 for production