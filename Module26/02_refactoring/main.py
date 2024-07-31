from collections.abc import Iterable

def generator(stop: int, object_1: list, object_2: list) -> Iterable:
    for x in object_1:
        for y in object_2:
            result = x * y
            yield x, y, result
            if result == stop:
                print('Found!!!')
                return

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
for x, y, result in generator(to_find, list_1, list_2):
    print(x, y, result)

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

# TODO провести рефакторинг кода

# Принято
