def print_numbers(num):
    if num != 1:
        print_numbers(num - 1)
    print(num)

numbers = int(input('Введите num: '))
print_numbers(numbers)
