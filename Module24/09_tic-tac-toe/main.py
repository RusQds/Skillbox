class Tic:
	win_dict= dict()
	location_dict = dict()
	win_combinations = [[1,2,3],[3,4,5],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

	def print_table(self, number=(-1), location=0):
		number = number % 2
		if number == 0:
			step = 'x'
		elif number == 1:
			step = 'o'
		count = 1
		print('_' * 13)
		for t in range(3):
			line = 0
			for i in range(3):
				line += 1
				for j in range(3):
					if line == 1:
						print('|   ', end='')
					elif line == 2:
						if count in self.location_dict:
							flag = self.location_dict[count]
						elif count != location:
							flag = count
						else:
							self.location_dict[location] = step
							flag = step
							if step in self.win_dict:
								self.win_dict[step].append(location)
							else:
								self.win_dict[step] = [location]
						count += 1
						print('| {} '.format(flag), end='')
					elif line == 3:
						print('|___'.format(1), end='')
				print('|')
		return step

	def win_check(self):
		for i_elem in self.win_dict:
			if len(self.win_dict[i_elem]) >= 3:
				for i in range(len(self.win_dict[i_elem])):
					for j in range(i + 1, len(self.win_dict[i_elem])):
						for t in range(j + 1, len(self.win_dict[i_elem])):
							list = [self.win_dict[i_elem][i],self.win_dict[i_elem][j],self.win_dict[i_elem][t]]
							if sorted(list) in self.win_combinations:
								return True

Tic().print_table()
number = -1
while True:
	number += 1
	if number % 2 == 0:
		location = int(input('ХОДЯТ КРЕСТИКИ. Введите номер клетки: '))
	else:
		location = int(input('ХОДЯТ НОЛИКИ. Введите номер клетки: '))

	step =Tic().print_table(number, location)
	flag = Tic().win_check()
	if flag:
		print('Победу одержали - {}'.format(step))
		break

# Принято
