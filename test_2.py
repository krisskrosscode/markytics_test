import logging


def setup_whatsapp_logger(name, log_file, level=logging.INFO):
    """To setup loggers for any callback function in this file"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


whatsapp_logger = setup_whatsapp_logger('wa_logger_name', 'whatsapp_callback_logs.log')

def test():
    print('test func')
    whatsapp_logger.info('sdgda')

test()