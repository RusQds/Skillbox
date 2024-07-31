def sum(*args, sum_numbers=0):
	for i_args in args:
		if isinstance(i_args, list):
			for i_number in i_args:
				if isinstance(i_number, list):
					sum_numbers = sum(i_number, sum_numbers=sum_numbers)
				else:
					sum_numbers += i_number
		else:
			sum_numbers += i_args
	return sum_numbers

print('Ответ: ', sum([[1, 2, [3]], [1], 3]))
print('Ответ: ', sum(1, 2, 3, 4, 5))

# Принято

