import time
from typing import Callable, Any

# TODO Возвращает Callable
def delay_func(func: Callable) -> Any:
    """ Эта функция замедляет работу на 3 секунды"""
    def wrap_func(*args, **kwargs):
        time.sleep(3)
        result = func()
        return result
    return wrap_func



@delay_func
def test():
    print('<Тут что-то происходит...>')

test()

# Принято
