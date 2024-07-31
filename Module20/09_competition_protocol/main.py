# # Долго думал над решением этой задачи, перебрал много разных вариантов возможного решения. В итоге пришел к этому.
# # Мне кажется решение есть более красивое, прошу Вас написать как стоило решить данную задачу.
#
name_list = ['69485 Jack', '95715 qwerty', '95715 Alex', '83647 M', '197128 qwerty', '95715 Jack', '93289 Alex',
						 '95715 Alex', '95715 M']
count_people = int(input('Сколько записей вносится в протокол? '))
people_point = dict()
win_players = dict()

print('Записи (результат и имя):')
for i in range(count_people):
	people = name_list[i].split(' ')
	# people = input('{0} запись: '.format(i + 1)).split(' ')
	if int(people[0]) not in people_point:
		people_point[int(people[0])] = [people[1]]
	elif people[1] not in people_point[int(people[0])]:
		people_point[int(people[0])].append(people[1])

number = 1
for point in reversed(sorted(people_point)):
	for player in people_point[point]:
		if player not in win_players and len(win_players) < 3:
			win_players[player] = point
			print('{place} место. {name} ({point})'.format(
				place=number,
				name=player,
				point=point
			))
			number += 1

# Мой вариант:
# name_list = ['69485 Jack', '95715 qwerty', '95715 Alex', '83647 M', '197128 qwerty', '95715 Jack', '93289 Alex',
# 						 '95715 Alex', '95715 M']
#
# records = [(int(record.split()[0]), record.split()[1]) for record in name_list]
# print(records)
# max_scores = {}
# for index, (score, name) in enumerate(records):
# 	if name not in max_scores or score > max_scores[name][1]:
# 		max_scores[name] = (index, score)
#
# sorted_keys = sorted(max_scores, key=lambda x: (-max_scores[x][1], max_scores[x][0]))
# print([(key, max_scores[key]) for key in sorted_keys[:3]])

# Принято
