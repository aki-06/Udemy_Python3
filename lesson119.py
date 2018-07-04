# ロギング

"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

logging.basicConfig(filename='info.log', level=logging.INFO)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')


logging.info('info {}'.format('test'))
# logging.info('info %s' % ('test'))
# logging.info('info %s %s', 'test', 'test2')