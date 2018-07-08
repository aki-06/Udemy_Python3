import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# loggerを使ったものはlogtest.logに書き込まれる
h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logger.info('from logtest')
    logger.debug('from logtest debug')