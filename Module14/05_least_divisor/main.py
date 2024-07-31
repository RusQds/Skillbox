
def divider(number):
	divider = 0
	count = 2
	while divider == 0:
		if number % count == 0:
			divider = count
			break
		else:
			count += 1
	return divider

number = int(input('Введите число:'))
print('Наименьший делитель, отличный от единицы:', divider(number))

# Принято
