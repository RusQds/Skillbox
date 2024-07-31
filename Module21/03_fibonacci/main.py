def fibonachi(num, first=0, second=1, step=1):
	if step == num:
		return second
	else:
		number = second
		second = first + second
		first = number
		step += 1
		return fibonachi(num, first, second, step)

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: {0}'.format(fibonachi(num_pos)))

# Принято
