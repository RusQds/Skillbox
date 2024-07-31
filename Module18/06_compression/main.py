

text = input('Введите строку: ')
new_text = ''
count = 1
for i in range(1, len(text)):
	if text[i] == text[i - 1]:
		count += 1
	else:
		new_text += text[i - 1] + str(count)
		count = 1
new_text += text[len(text) - 1] + str(count)

print('Закодированная строка:', new_text)

# Принято
