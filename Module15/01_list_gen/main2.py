n = int(input('Введите число n: '))
new_list = [num for num in range(1, n + 1) if num % 2 == 1]
print(new_list)