'''
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата. Клиент и сервер должны быть реализованы в виде отдельных скриптов,
содержащих соответствующие функции.
Функции клиента:
сформировать presence-сообщение; отправить сообщение серверу;
получить ответ сервера; разобрать сообщение сервера; параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту; отправляет ответ клиенту; имеет параметры командной строки: -p <port> — TCP-порт для работы
 (по умолчанию использует 7777); -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
'''

from socket import  *
import pickle
import time


s = socket(AF_INET, SOCK_STREAM)

def start_soc():
    s.bind(('',7777))
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)


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
        print('Server does not work')