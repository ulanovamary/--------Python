import logging
import logging.handlers


formatter = logging.Formatter(
    '%(asctime)s %(levelname)-10s %(module)s %(message)s'
    )

log_handler = logging.handlers.TimedRotatingFileHandler('server.log', when='D', interval=1, backupCount=2)
log_handler.setFormatter(formatter)

logger = logging.getLogger('msnger_server')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

def to_console():
    to_cons = logging.StreamHandler()
    to_cons.setLevel(logging.NOTSET)
    to_cons.setFormatter(formatter)
    logger.addHandler(to_cons)
    logger.info('this info is from server logger to console')

if __name__ == '__main__':
    to_console()