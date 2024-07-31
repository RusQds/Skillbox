def min_diff(number):
    diff_list = [num for num in range(2, number + 1) if number % num == 0]
    min_number = min(diff_list)
    return min_number

number = int(input('Введите число: '))
min_number = min_diff(number)
print(f'Наименьший делитель, отличный от единицы: {min_number}')