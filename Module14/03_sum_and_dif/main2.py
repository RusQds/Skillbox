def sum_numbers(number):
    sum_num = sum([int(num) for num in str(number)])
    return sum_num

def count_numbers(number):
    count_num = len([int(num) for num in str(number)])
    return count_num

my_number = int(input('Введите число: '))
if type(my_number) == int:
    first_function = sum_numbers(my_number)
    second_function = count_numbers(my_number)
    diff_num = first_function - second_function
    print(f'Сумма цифр: {first_function}')
    print(f'Кол-во цифр в числе: {second_function}')
    print(f'Разность суммы и кол-ва цифр: {diff_num}')
else:
    print('Вы ввели не число!')