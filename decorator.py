'''
1. Продолжая задачу логирования, реализовать декоратор @log, фиксирующий обращение к декорируемой функции.
Он сохраняет ее имя и аргументы.
2. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная. Если имеется такой код:
@log
def func_z():
 pass

def main():
 func_z()
...в логе должна быть отражена информация:
"<дата-время> Функция func_z() вызвана из функции main"
'''
import logging
import functools


logger = logging.getLogger('deco_log')


logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
log_format = "%(asctime)s - %(name)s - %(levelname)s -- %(message)s"
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

def log(func_to_log):
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}.')
        return ret
    return log_saver


#class LogDecorator(object):
#    def __init__(self):
#        self.logger = logging.getLogger('decorator-log')
#    def __call__(self, fn):
#        @functools.wraps(fn)
#        def decorated(self=None, *args, **kwargs):
#            try:
#                self.logger.debug(f'{fn.__name__} - {args} - {kwargs}')
#                result = fn(*args, **kwargs)
#                self.logger.debug(result)
#                return result
#            except Exception as e:
#                self.logger.debug("Exception {0}".format(e))
#                raise e
#            return result
#        return decorated


