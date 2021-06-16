import les3_cli
import socket
import pytest

#@pytest.mark.parametrize("addr, port", [('', 7777),
#                                        ('localhost',7777),])
#def test_to_start_les3_serv(addr, port):
#    to_start_serv = les3_cli.start_soc()
#    to_start_serv(addr, port)

#@pytest.mark.parametrize("addr, port", [('', 7777),
 #                                       ('localhost',7777),])

def test_connection_positive():
    assert les3_cli.start_soc() == True


def test_to_start_les3_serv():
    to_start_serv = les3_cli.start_soc()
    to_start_serv('wrong_addr', 'wrong_port')

def test_answer_to_send():
   data = les3_cli.answer_to_send()


def main():
    test_to_start_les3_serv()
    test_answer_to_send()




if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('wrong test')