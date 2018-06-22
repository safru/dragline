MAX_RETRY = 20
# UNIQUE_CHECK = True
THREADS = 50

# REQUEST_PROCESSOR = 'dragline.http:RequestProcessor'

DEFAULT_REQUEST_ARGS = {
    # 'allow_redirects': True,
    # 'auth': None,
    # 'cert': None,
    # 'cookies': None,
    # 'data': None,
    # 'files': None,
    'headers': {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
    # 'json': None,
    # 'method': None,
    # 'params': None,
    'proxy': None,
    # 'stream': False,
    'timeout': 20,
    # 'verify': False
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'dragline': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        '2386_steinerturf': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

try:
    from local_settings import *
except:
    pass

