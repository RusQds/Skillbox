import random

#Вроде поправил, все работает вроде корректно.
#Добавил для автотеста генерацию списков.

skates = [random.randint(20, 50) for _ in range(random.randint(1, 10))]
peoples = [random.randint(20, 50) for _ in range(random.randint(1, 10))]
count = 0

print('\nВсего на складе коньков: ',len(skates), '\nРазмеры коньков на складе: ', skates)
print('\nВсего желающих покататься: ',len(peoples), '\nРазмеры ног посетителей: ', peoples)
print()

# count_skates = int(input('\nКол-во коньков: '))
# for i in range(count_skates):
# 	skates.append(int(input('Размер ' + str(i + 1) + ' пары: ')))
#
# count_peoples = int(input('\nКол-во людей: '))
# for n in range(count_peoples):
# 	peoples.append(int(input('Размер ноги ' + str(n + 1) + ' человека: ')))

for _ in range(len(peoples)):
	if max(peoples) <= max(skates):
		count += 1
		print('Человек с размером ноги', max(peoples), 'наденет коньки с размером', max(skates))
		skates.remove(max(skates))
		peoples.remove(max(peoples))
	else:
		print('Человек с размером ноги', max(peoples), 'будет ходить пешком=(')
		peoples.remove(max(peoples))
	if len(skates) == 0:
		print('Коньки закончились')
		break

print('Наибольшее кол-во людей, которые могут взять ролики:', count)
print('Оставшиеся коньки - ', skates)
