count_numbers = int(input('Введите длину списка: '))
numbers_list = [(1 if n % 2 == 0 else n % 5) for n in range(count_numbers)]
print(f'Результат:  {numbers_list}')