
def separator(object, sym):
	index_box = [index_object for index_object, j_object in enumerate(object) if j_object == sym]
	new_object = tuple()
	if len(index_box) >= 2:
		new_object = object[index_box[0]:index_box[1] + 1]
	elif len(index_box) == 1:
		new_object = object[index_box[0]:]
	return new_object

object = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
sym = int(input('Введите элемент: '))

print('Ответ в консоли:', separator(object, sym))

# Принято
