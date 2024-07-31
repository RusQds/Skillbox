def new_tuple(first, second):
	first = list(first)
	second = list(second)
	zip_list = ((first[i], second[i]) for i in range(min(len(first), len(second))))
	return zip_list

first = 'abcdejs'
second = (10, 20, 30, 40, 50)
a = {1: 'a', 2: 'b', 3: 'c'}

print('Строка: {0}'.format(first))
print('Кортеж чисел: {0}'.format(second))
print(new_tuple(first, second))
for tuple_item in new_tuple(first, second):
	print(tuple_item)

# Принято
