from typing import Callable, Any
import functools

def debug(func: Callable) -> Any:
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        #Не разобрался как красиво оформить вывод аргов и кваргов.
        print('Вызывается {name} ({args}, {kwargs})'.format(name=func.__name__, args=args, kwargs=kwargs))
        result = func(*args, **kwargs)
        print('{name} вернула значение {result}'.format(name=func.__name__, result=result))
        print(result)
        print()
        return result
    return wrap_func

@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# Принято
