from collections.abc import Iterable


class NumberIterator:
    def __init__(self, number: int) -> None:
        self.__start_number = -1
        self.__stop_number = number

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__start_number < self.__stop_number:
            self.__start_number += 1
            return self.__start_number ** 2
        else:
            raise StopIteration


def number_iterator(number: int) -> Iterable[int]:
    for num in range(number + 1):
        yield num ** 2


count_number = int(input('Введите число: '))

number_iterator1 = NumberIterator(count_number)
for elem in number_iterator1:
    print(elem.__str__())

number_iterator2 = number_iterator(count_number)
for elem in number_iterator2:
    print(elem)
number_iterator3 = [num ** 2 for num in range(0, count_number + 1)]
for elem in number_iterator3:
    print(elem)
