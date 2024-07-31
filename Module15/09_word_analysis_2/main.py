text = input('Введите слово:')
flag = True
for i in range(len(text)):
	if text[i] != text[-1 - i]:
		flag = False
		break

if flag == True:
	print('Слово является палиндромом')
else:
	print('Слово не является палиндромом')

# Принято
