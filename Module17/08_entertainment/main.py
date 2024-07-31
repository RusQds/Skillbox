import random

def sticks_line(sticks):
	sticks_line = ''
	for i in sticks:
		sticks_line += i
	return sticks_line
# N = int(input('Кол-во палок: '))
# K = int(input('Кол-во бросков: '))
N = random.randint(1, 20)
K = random.randint(1, 5)
print('Кол-во палок:', N)
print('Кол-во бросков:', K)

sticks = ['I' for i in range(N)]
stones = [[random.randint(1,N), random.randint(1,N)] for _ in range(K)]

print('\nНачальная расстановка палок:', sticks_line(sticks))

for i in range(K):
	print('\nБросок', str(i + 1) + '.', 'Сбиты палки с номера', min(stones[i]), 'по номер', max(stones[i]))
	for j in range(min(stones[i]) - 1, max(stones[i])):
		sticks[j] = '.'
	print('Результат:', sticks_line(sticks))
	if sticks.count('I') == 0:
		print('Вы сбили все палки!')
		break

# Принято
