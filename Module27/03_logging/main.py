import datetime
from typing import Callable, Any
import functools

def logging(func: Callable) -> Any:
    """Функция логирует ошибки"""
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        try:
            print(func.__name__, '\n', func.__doc__)
            result = func()
            return result
        except:
            print('Возникла ошибка, записываем в function_errors.log')
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write('{time} - Возникла ошибка {error} в функции {func}\n'.format(
                    time=datetime.datetime.today(),
                    error='ОШИБКА', #Не разобрался как вытягивать в переменную название ошибки
                    func=func.__name__
                ))
    return wrap_func

@logging
def test1():
    """Какая то функция 1"""
    print('<Тут что-то происходит...>')

@logging
def test2():
    """Какая то функция 2"""
    raise Exception
    print('<Тут что-то происходит...>')

@logging
def test3():
    """Какая то функция 3"""
    print('<Тут что-то происходит...>')

test1()
test2()
test3()

# Принято
