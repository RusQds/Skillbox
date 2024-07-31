def sumNumbers(number1, number2):
	sumNumbers = number1 + number2
	return sumNumbers

def coup(number):
	reNumber = ''
	while int(number) != 0:
		reNumber += str(int(number) % 10)
		number = int(number) // 10
	return reNumber

def reNumbers(number):
	firstNumber = ''
	secondNumber = ''
	flag = True
	for i in str(number):
		if i == '.':
			flag = False
		else:
			if flag == True:
				firstNumber += i
			else:
				secondNumber += i
	reNumber = float(coup(int(firstNumber)) + '.' + coup(int(secondNumber)))
	return reNumber

firstNumber = float(input('Введите первое число:'))
secondNumber = float(input('Введите второе число:'))
print('Первое число наоборот:', reNumbers(firstNumber))
print('Второе число наоборот:', reNumbers(secondNumber))
print('Сумма:', sumNumbers(reNumbers(firstNumber), reNumbers(secondNumber)))

# Принято
