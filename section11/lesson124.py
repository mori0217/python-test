import logging

logging.basicConfig(level=logging.DEBUG)


class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())

logger.info('from main')
logger.info('from main password:abc123')
logger.info('from main abc123')
