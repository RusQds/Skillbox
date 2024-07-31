def hanoi(numbers, x, y, z):
	if (numbers) == 1:
		print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(numbers, x, z))
		return
	hanoi(numbers - 1, x, z, y)
	print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(numbers, x, z))
	hanoi(numbers - 1, y, x, z)

count = int(input('Введите количество дисков: '))

hanoi(count, '1', '2', '3')

# Принято
