def quest(numbers_dict):
	# TODO Проще и эффективнее в этой задаче было бы использовать множества (set) вместо словарей
	#  Например, пусть у нас есть начальное множество всех чисел, которые мог бы загадать Артем
	#  possible_numbers = set(range(1, max_number + 1))
	#  пусть numbers - это множество чисел, которые ввел пользователь
	#  Тогда, если ответ Артема "нет", мы убираем эти числа из possible_numbers:
	#  possible_numbers = possible_numbers - numbers
	#  А если ответ "да", то оставляем в possible_numbers только те числа, которые есть в обоих множествах:
	#  possible_numbers = possible_numbers & numbers
	new_numbers_dict = dict()
	numbers_list = input('\nНужное число есть среди вот этих чисел: ')
	# TODO Программа может работать бесконечно
	#  Потому лучше здесь было бы использовать циклы, а не рекурсию
	#  Если попадется очень несообразительный игрок, то спустя около 900 попыток программа выдаст ошибку,
	#  т.к. рекурсия достигнет максимальной глубины
	if numbers_list == 'Помогите!':
		print('Артём мог загадать следующие числа:', end = ' ')
		for t in numbers_dict.keys():
			print(t, end = ' ')
		quest(numbers_dict)
	else:
		flag = input('Ответ Артёма: ').lower()
		if flag == 'нет':
			for i in numbers_list.split(' '):
				if i in numbers_dict.keys():
					numbers_dict.pop(i)
			quest(numbers_dict)
		elif flag == 'да' and len(numbers_list.split(' ')) == 1:
			print('Поздравляю, ты угадал!')
		else:
			for i in numbers_list.split(' '):
				if i in numbers_dict.keys():
					new_numbers_dict[i] = ''
			numbers_dict.clear()
			numbers_dict.update(new_numbers_dict)
			quest(numbers_dict)

max_number = int(input('Введите максимальное число: '))
numbers_dict = dict()

for i in range(max_number + 1):
	numbers_dict[str(i)] = ''

quest(numbers_dict)

# Принято
