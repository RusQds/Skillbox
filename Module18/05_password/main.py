def upper_count(list_sim):
	numbers = [str(i) for i in range(0, 10)]
	list_upper_sim = [i for i in list_sim if i.upper() == i and i not in numbers]
	return len(list_upper_sim)

def number_count(list_sim):
	numbers = [str(i) for i in range(0, 10)]
	list_numbers = [i for i in list_sim if i in numbers]
	return len(list_numbers)

while True:
	password = input('Придумайте пароль: ')
	if len(password) < 8 or upper_count(password) < 1 or number_count(password) < 3:
		print('Пароль ненадёжный. Попробуйте ещё раз.')
	else:
		print('Это надёжный пароль!')
		break

# Принято
