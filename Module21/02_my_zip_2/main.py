#Не до конца смог разобрать задание, а в чем отличие от прошлого 10? Надо было это сделать как то с применением
# рекурсии?

def min_len(x, y):
	return min(len(x), len(y))

def zip_clone(obj1, obj2):
	obj1, obj2 = list(obj1), list(obj2)
	zip_tuple =((obj1[i], obj2[i]) for i in range(min_len(obj1, obj2)))
	return zip_tuple






a = 'sdf'
b = [1, 2, 3, 4, 5]
c = (1, 2, 3, 4, 5)
d = {1, 2, 3, 4, 5, 6}
e = {1: 2, 3: 4, 5: 6}


print(list(zip_clone(e, d)))

# Принято
