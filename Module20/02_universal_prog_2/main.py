def is_prime(number):
	if number != 0 and number != 1:
		for i_number in range(2, number):
			if number % i_number == 0:
				return False
		return True
	else:
		return False
# Не смог разобраться как сделать обработку словаря, что бы в список при соблюдении условия добавлялся Ключ: Значение.
# Были мысли добавить .items, но тогда необходимо добавлять проверку на то что это словарь, и я сомневаюсь что такой
# метод был бы корректным.
# TODO В случае со словарем должны добавляться только ключи, у вас все верно
#	 Чтобы добавлять пары ключ-значение, то да, нужно будет делать проверку на dict, что действительно
#	 не очень хорошо - это сделает программу менее расширяемой
def crypto(old_object):
	new_object = []
	for i_number, i_object in enumerate(old_object):
		if is_prime(i_number):
			new_object.append(i_object)
	return new_object


# object = 'О Дивный Новый мир!'
# object = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
object = {0: 1, 1: 2, 2: 3}


print(object)
print('Ответ в консоли: {0}'.format(crypto(object)))

# Принято
