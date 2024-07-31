alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = str.lower(input('Введите сообщение: '))
step = int(input('Введите сдвиг: '))
a_list = [str.lower(i) for i in alphabet]
new_text = ''

new_text_list = [(a_list[(a_list.index(i) + step) % len(a_list)] if i in a_list else i) for i in text]
for i in new_text_list:
	new_text += i

print(new_text)

# Принято
