import functools
from typing import Callable, Any

def counter(func: Callable) -> Any:
    my_func = {}
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        if func.__name__ in my_func:
            my_func[func.__name__] += 1
        else:
            my_func[func.__name__] = 1
        print('Функция {name} вызывалась {count} раз.'.format(name=func.__name__, count=my_func[func.__name__]))
        result = func()
        return result
    return wrap_func

@counter
def test1():
    """Какая то функция 1"""
    print('<Тут что-то происходит...>')

@counter
def test2():
    """Какая то функция 2"""
    print('<Тут что-то происходит...>')

@counter
def test3():
    """Какая то функция 3"""
    print('<Тут что-то происходит...>')

test1()
test1()
test2()
test3()
test3()
test3()

# Принято
