count = int(input('Кол-во клеток: '))
cell =[]

for i in range(count):
	cell.append(input('Эффективность ' + str(i + 1) + ' клетки: '))

for i in range(len(cell)):
	if i > int(cell[i]):
		print('Неподходящее значения:', cell[i])

# Принято
