import logging

PORT = 8000
HOST = '127.0.0.1'
CHECKING_TIMEOUT = 0.5

LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['stdout'],
            'level': logging.DEBUG,
            'propagate': True,
        },
    }
}
