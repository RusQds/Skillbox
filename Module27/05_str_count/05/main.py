from typing import Callable
import functools


def counter(funk: Callable) -> Callable:
    my_dict = {}

    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        func_name = funk.__name__
        if func_name in my_dict:
            my_dict[func_name] += 1
        else:
            my_dict[func_name] = 1
        print('Функция {func_name} вызывалась {count} раз(а)!'.format(func_name=func_name,
                                                                   count=my_dict[func_name]))
        return funk(*args, **kwargs)
    return wrapper


@counter
def test1():
    return 'test'


@counter
def test2():
    return 'test'


@counter
def test3():
    return 'test'


test1()
test2()
test2()
test3()
test3()
test3()
test1()
