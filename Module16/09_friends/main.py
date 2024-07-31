bank =[]
count_friends = int(input('Кол-во друзей: '))
count_credits = int(input('Долговых расписок: '))


for i in range(count_credits):
	print('\n', i + 1, 'расписка')
	bank.append([int(input('Кому: ')), int(input('От кого: ')), int(input('Сколько: '))])

print('\nБаланс друзей:')
for n in range(1, count_friends + 1):
	credit = 0
	for m in bank:
		if n == m[0]:
			credit -= m[2]
		if n == m[1]:
			credit += m[2]
	print(n, end=': ')
	print(credit)

# Принято
