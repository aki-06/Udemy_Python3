# ロギング　フォーマッタ
import logging

formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info %s', 'test')