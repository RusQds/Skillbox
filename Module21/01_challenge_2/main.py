def print_num(num, start=1):
	if start != num:
		print(start)
		start += 1
		print_num(num, start)
	else:
		print(start)

num = int(input('Введите num: '))
print_num(num)

# Принято
