import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('section11/log_test.log')
logger.addHandler(h)


def do_something():
    logger.info('test info')
    logger.debug('test debug')
