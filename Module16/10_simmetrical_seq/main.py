
count = 0
list_numbers = []
count_number = int(input('Кол-во чисел: '))
for _ in range(count_number):
	list_numbers.append(int(input('Число: ')))


print('Последовательность:', end = ' ')

for i in list_numbers:
	print(i, end = ' ')

for n in range(len(list_numbers)):
	for i in range(len(list_numbers) - n):
		if list_numbers[n + i] != list_numbers[-1 - i]:
			count += 1
			break

print('\nНужно приписать чисел:', count)

print('Сами числа:', end = ' ')

for i in range(count - 1, -1, -1):
	print(list_numbers[i], end = ' ')
	list_numbers.append(list_numbers[i])

print('\nНовая последовательность', end = ' ')
for i in list_numbers:
	print(i, end = ' ')

# Принято
