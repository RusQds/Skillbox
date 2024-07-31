def new_contact(contact_dict):
		name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split(' '))
		if (name[0], name[1]) not in contact_dict:
			tel = input('Введите номер телефона: ')
			contact_dict[name[0], name[1]] = tel
			print('Контакт успешно добавлен!')
			print('Текущий словарь контактов: {dict}'.format(dict=contact_dict))
		else:
			print('Такой человек уже есть в контактах.')
			print('Текущий словарь контактов: {dict}'.format(dict=contact_dict))

def serch_contact(contact_dict):
	surname = input('Введите фамилию для поиска: ')
	for people, tel in contact_dict.items():
		if surname.lower() == people[1].lower():
			print(people[0], people[1], tel)

contact_dict = dict()

while True:
	command = int(input('Введите номер действия: \n1. Добавить контакт \n2. Найти человека \n=> '))
	if command == 1:
		new_contact(contact_dict)
	elif command == 2:
		serch_contact(contact_dict)
	else:
		print('Ошибка ввода команды! Повторите попытку\n')

# Принято
