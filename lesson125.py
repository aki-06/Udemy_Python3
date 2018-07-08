# ロギングの書き方

import logging

def main():
    logger = logging.getLogger(__name__)
    logger.error('Api call is failed')
    logger.error({
        'action': 'create',
        'status': 'fail',
        'message': 'Api call is failed'
    })


if __name__ == '__main__':
    main()