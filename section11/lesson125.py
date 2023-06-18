import logging.config

# logging.config.fileConfig('section11/logging.ini')
logging.config.dictConfig({
    'version': 1,
    "formatters": {
        "sampleFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "sampleHandlers": {
            "class": "logging.StreamHandler",
            "formatter": "sampleFormatter",
            "level": logging.DEBUG,
        }
    },
    "root": {
        "handlers": ["sampleHandlers"],
        "level": logging.WARNING,
    },
    "loggers": {
        "section11": {
            "handlers": ["sampleHandlers"],
            "level": logging.DEBUG,
            "propagate": 0,
        },
    },
})
logger = logging.getLogger("section11")

logger.debug('test debug')
logger.info('test info')
logger.warning('test warning')
logger.error('test error')
logger.critical('test critical')
