def family_serch(family_db, family):
	for i_family, i_age in family_db.items():
		if family in i_family[0] or i_family[0] in family:
			print(i_family[0], i_family[1], i_age)


family_db = {
	('Сидоров', 'Игорь'): 24,
	('Сидоров', 'Олег'): 48,
	('Сидорова', 'Анждела'): 17,
	('Андреев', 'Влад'): 52,
	('Андреева', 'Ольга'): 14,
	('Иванов', 'Сергей'): 81,
	('Иванова', 'Оксана'): 36,
	('Иванова', 'Вика'): 28,
	('Петров', 'Алексей'): 18,
	('Соколова', 'Света'): 4,
	('Соколов', 'Сергей'): 25,
	('Соколов', 'Денис'): 21,
}

family = input('Введите фамилию: ')
family_serch(family_db, family)

# Принято
