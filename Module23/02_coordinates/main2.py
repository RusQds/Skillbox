import random
import os

def read_file(path):
    with open(path, 'r', encoding='utf-8') as open_file:
        for elem in open_file.read().split('\n'):
            elem_list = elem.split()
            first_number = first_funk(int(elem_list[0]), int(elem_list[1]))
            second_number = second_funk(int(elem_list[0]), int(elem_list[1]))
            random_int = random.randint(0,100)
            sorted_list = [str(random_int), str(first_number), str(second_number)]
            sorted_list.sort()
            with open('result2.txt', 'a', encoding='utf-8') as result_file:
                result_file.write(f'{sorted_list}\n')
def first_funk(x, y):
    result = 0
    try:
        x += random.randint(0,5)
        y += random.randint(0,10)
        result = x / y
    except ZeroDivisionError:
        print('Деление на 0!')
    finally:
        return result

def second_funk(x, y):
    result = 0
    try:
        x -= random.randint(0,5)
        y -= random.randint(0,10)
        result = y / x
    except ZeroDivisionError:
        print('Деление на 0!')
    finally:
        return result

path = os.path.abspath('coordinates.txt')
read_file(path)