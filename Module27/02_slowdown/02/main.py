import functools
import time
from typing import Callable, Any


def pause_func(funk: Callable) -> Any:

    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        for t in range(5):
            print('Идет {time} секунда остановки!'.format(time=t+1))
            time.sleep(1)
        return funk(*args, **kwargs)
    return wrapper


@pause_func
def test():
    print('<Тут что-то происходит...>')


test()
