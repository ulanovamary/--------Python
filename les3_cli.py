'''
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции. Функции клиента: сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777. Функции сервера: принимает сообщение клиента;
формирует ответ клиенту; отправляет ответ клиенту; имеет параметры командной строки: -p <port> — TCP-порт для работы
 (по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
'''
import argparse
from socket import *
import pickle
import time


s = socket(AF_INET, SOCK_STREAM)

def start_soc(addr='localhost', port=7777):
    s.connect((addr,port))
    #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


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



