import functools
from typing import Callable


def debug(funk: Callable) -> Callable:
    """Функция дебаг"""

    @functools.wraps(funk)
    def wrapper(*args, **kwargs) -> None:
        func_name = funk.__name__
        if args and kwargs:
            func_name = '{}({}, {})'.format(func_name, ', '.join(args), ', '.join(kwargs))
        elif args:
            func_name = '{}({})'.format(func_name, ', '.join(args))
        elif kwargs:
            func_name = '{}({})'.format(func_name, ', '.join(kwargs))

        print('Вызывается {func_name}'.format(func_name=func_name))
        result = funk(*args, **kwargs)
        print('{func_name} вернула значение {result}'.format(func_name=func_name, result=result))
        print(result)

    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
