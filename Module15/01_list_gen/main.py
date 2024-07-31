finish_number = int(input('Введите число N: '))
my_list = []

for i in range(1, finish_number + 1):
	if i % 2 != 0:
		my_list.append(i)

print(my_list)

# Принято
