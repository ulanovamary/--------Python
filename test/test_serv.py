import les3_serv
import pytest

def main():
    test_to_start_les3_serv()
#@pytest.mark.parametrize("addr, port", [('', 7777),
#                                        ('localhost',7777),])
#def test_to_start_les3_serv(addr, port):
#    to_start_serv = les3_serv.start_soc()
#    to_start_serv(addr, port)

def test_to_start_les3_serv():
    to_start_serv = les3_serv.start_soc()
    to_start_serv('wrong_addr', 'wrong_port')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('wrong test')