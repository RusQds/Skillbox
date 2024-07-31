guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
	print('Сейчас на вечеринке', len(guests), 'человек:', guests)
	door = input('Гость пришел или ушел? ')
	if door == 'пришел':
		guest = input('Имя гостя: ')
		if len(guests) < 6:
			guests.append(guest)
			print('Привет,', guest)
		else:
			print('Прости,', guest, ', но мест нет.')
	elif door == 'ушел':
		guest = input('Имя гостя: ')
		guests.remove(guest)
		print('Пока,', guest)
	elif door == 'Пора спать':
		print('Вечеринка закончилась, все легли спать.')
		break
	else:
		print('Ошибка ввода, попробуйте заново')

# Принято
