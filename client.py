from socket import *
import pickle
import time
import  logging
import log.client_log_config
from decorator import log


logger = logging.getLogger('msnger_client')


s = socket(AF_INET, SOCK_STREAM)

@log
def start_soc(addr='localhost', port=7777):
    try:
        s.connect((addr,port))
    except Exception as e:
        logger.critical(f'Соединение не установлено. Обнаружена ошибка {e}')
    else:
        logger.info('Соединение клиента с сервером установлено')
        return s
    #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

@log
def answer_to_send():
    msg = {
        "action": "authenticate",
        "time": time.time(),
        "user": {
            "account_name": "ACC_name",
            "password": "Password"
        }
    }
    s.send(pickle.dumps(msg))
    data=s.recv(1024)
    s.close()
    print('Server:' + str(pickle.loads(data)))


if __name__ =='__main__':
    socket = start_soc()
    to_send = answer_to_send()



