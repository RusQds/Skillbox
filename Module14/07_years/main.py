def countNumbers(number):
	for i in str(number):
		count = 0
		for n in str(number):
			if n == i:
				count += 1
		if count >= 3:
			print(number)
			break

def LackyYear():
	firstYear = int(input('Введите первый год:'))
	secondYear = int(input('Введите второй год:'))
	if firstYear < 100 or secondYear < 100:
		print('Ошибка ввода! Год должен быть больше 99')
		LackyYear()
	else:
		minYear = min(firstYear, secondYear)
		maxYear = max(firstYear, secondYear)
		for i in range(minYear, maxYear + 1):
			countNumbers(i)

LackyYear()

# Принято
