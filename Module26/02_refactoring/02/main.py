from collections.abc import Iterable

# Нужно найти какие два числа из списков в результате попарного перемножения дадут число 56
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def can_continue1(list_1: list, list_2: list, to_find: int) -> Iterable[int]:
    for x in list_1:
        for y in list_2:
            yield x, y, x * y
            if x * y == to_find:
                print('Found!!!')
                return




my_iterable = can_continue1(list_1, list_2, to_find)
for x, y, result in my_iterable:
    print(x, y, result)