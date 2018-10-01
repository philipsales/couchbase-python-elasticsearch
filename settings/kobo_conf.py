
#SERVER Configuration
KoboENV = "development"

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
        'FORM': '13'
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
        'USERNAME': 'koboadmin',
        'PASSWORD': 'AWH~adm!n123',
        'PROTOCOL': 'https',
        'SCHEME': 'kobo',
        'IP': '',
        'HOST': 'kc.curis.online',
        'PORT': '',
        'VERSION':'v1',
        'TIMEOUT': 7200,
        'FORM': '3'
    }
}