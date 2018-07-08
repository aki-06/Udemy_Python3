# ロギング　フィルタ
import logging

logging.basicConfig(level=logging.INFO)

class NoPassFilter(logging.Filter):
    def filter(self, record):
        """
        passedという文字がlogにあったら出力しない
        """
        log_message = record.getMessage()
        return 'passwd' not in log_message

logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main xxx = aaa')
logger.info('from main passwd = test')
