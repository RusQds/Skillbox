
first_text = list(input('Первая строка:'))
second_text = list(input('Вторая строка:'))
count = 0

for i in range(len(first_text)):
	if first_text == second_text:
		break
	else:
		count += 1
		second_text.append(second_text[0])
		second_text.remove(second_text[0])
		print(second_text)

if first_text == second_text:
	print('Первая строка получается из второй со сдвигом', count)
else:
	print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

# Принято
