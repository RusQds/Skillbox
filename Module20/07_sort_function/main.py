def tpl_sort(origin_tuple):
	numbers_tuple = tuple(sorted(origin_tuple[:]))
	for i_number in numbers_tuple:
		# TODO Проверять на целое число лучше с помощью isinstance()
		#  тем более в кортеже могут содержаться строки, словари, не только int или float
		if not isinstance(i_number, int):
			return origin_tuple
	return numbers_tuple

# def tpl_sort(origin_tuple):
# 	numbers_list = list(origin_tuple[:])
# 	new_numbers_list = list()
# 	for i_number in range(len(numbers_list)):
# 		if min(numbers_list) % 1 != 0:
# 			return origin_tuple
# 		else:
# 			new_numbers_list.append(numbers_list.pop(numbers_list.index(min(numbers_list))))
# 	return tuple(new_numbers_list)



origin_tuple = (6, 3, -1, 8, 4, 10, -5)
print('Оригинальный кортеж:', origin_tuple)
print('Ответ в консоли:', tpl_sort(origin_tuple))

# Принято
