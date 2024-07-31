import random


max_number = int(input('Введите максимальное число: '))
my_number = random.randint(1, max_number)
actual_nambers = {str(i) for i in range(1, max_number + 1)}

while True:
    numbers_set = set(input('Нужное число есть среди вот этих чисел: ').split())
    if len(numbers_set) != 1 and str(my_number) in numbers_set:
        print('Ответ Артёма: Да')
        actual_nambers = numbers_set.intersection(actual_nambers)
    elif len(numbers_set) == 1 and str(my_number) in numbers_set:
        print('Ответ Артёма: Угадал')
        break
    elif ''.join(numbers_set).lower() == 'помогите!':
        print('Артём мог загадать следующие числа: {0}'.format(actual_nambers))
    else:
        print('Ответ Артёма: Нет')
        actual_nambers = actual_nambers.difference(numbers_set)