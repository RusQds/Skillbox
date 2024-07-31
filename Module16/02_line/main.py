first_min = 160
first_max = 176
second_min = 162
second_max = 180

first_class = list(range(first_min, first_max + 1, 2))
second_class = list(range(second_min, second_max + 1, 3))
print('Список первого класса по возрастанию роста', first_class)
print('Список второго класса по возрастанию роста', second_class)

first_class.extend(second_class)

for i in range(len(first_class)):
	for n in range(i, len(first_class)):
		if first_class[i] > first_class[n]:
			first_class[i], first_class[n] = first_class[n], first_class[i]

print('Общий список двух классов по возрастанию роста', first_class)

# Принято
