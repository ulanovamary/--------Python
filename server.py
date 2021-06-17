from socket import  *
import pickle
import argparse
import logging

logger = logging.getLogger('msnger_server')


s = socket(AF_INET, SOCK_STREAM)

def start_soc(addr='', port=7777):
    s.bind((addr, port))
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    try:
        s.listen()
    except Exception as e:
        logger.critical(f'Ошибка инициализации сервера {e}')
    else:
        logger.info('Инициализация сервера прошла успешно')

def arg_parse(ADDRESS='', PORT=7777):
    parser = argparse.ArgumentParser(description='IP,PORT parser')
    parser.add_argument("-addr", default=ADDRESS)
    parser.add_argument("-port", default=PORT, type=int)
    return parser.parse_args()


def main():
    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))
        data = client.recv(1024)
        response = {
            'response': 200,
        }
        client.send(pickle.dumps(response))
        client.close()


if __name__ == '__main__':
    socket = start_soc()
    try:
        main()
    except Exception as e:
        print('Server did not start')