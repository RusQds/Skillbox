from typing import Callable, Any
import functools

# TODO Декоратор возвращает Callable
def how_are_you(func: Callable) -> Any:
    """
    Функция выполняет какую то фигню.
    """
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        quest = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func()
        return result
    return wrap_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# Принято
