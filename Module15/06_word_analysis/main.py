text = input('Введите слово: ')
text_list = []

for i in text:
	if i not in text_list:
		text_list.append(i)

print('Кол-во уникальных букв:', len(text_list))

# Принято
