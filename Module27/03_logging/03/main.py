import functools
import datetime
import traceback
from typing import Callable, Any


def logging(func: Callable) -> Any:
    """Функция логирует ошибки"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as exception:
            with open('function_errors.log', 'a', encoding='utf-8') as f:
                f.write('{time} - Возникла ошибка {error} в функции {func}\n'.format(
                    time=datetime.datetime.today(),
                    error=exception.__class__.__name__,
                    func=func.__name__
                ))
    return wrapper


@logging
def test1():
    """Какая то документация 1"""
    print(test1.__str__())
    print(test1.__doc__)


@logging
def test2():
    """Какая то документация 2"""
    print(test2.__str__())
    print(test2.__doc__)
    raise Exception


@logging
def test3():
    """Какая то документация 3"""
    print(test3.__str__())
    print(test3.__doc__)


test1()
test2()
test3()
