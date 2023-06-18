import logging
import logtest

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.info('main info')

logtest.do_something()
