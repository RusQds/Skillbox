import random

def clear_file():
	with open('out_file.txt', 'w') as file:
		file.write('')

def save_file(number):
	with open('out_file.txt', 'a') as file:
		file.write('{}\n'.format(str(number)))

count = 0
try:
	clear_file()
	while count < 777:
		number = int(input('Введите число: '))
		r = random.randint(1, 13)
		if r == 13:
			raise Exception
		else:
			count += number
			save_file(number)
	print('Вы успешно выполнили условие для выхода из порочного цикла!')
except Exception:
	print('Вас постигла неудача!')

# Принято


