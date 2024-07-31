from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Any:
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        question = input('“Как дела? ')
        print('{question}? А у меня не очень! Ладно, держи свою функцию.'.format(question=question))
        return func(*args, **kwargs)
    return wrap_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
