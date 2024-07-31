import time

text = input('Введите фразу: ')
shift = int(input('Сдвиг: '))
old_list = []
new_list = []

for i in text:
	old_list.append(i)

print('Изначальный список: ', old_list)
while True:
	for i in range(len(old_list)):
		new_list.append(old_list[0 - (shift % len(old_list)) + i])
	print('Сдвинутый список:', new_list)
	old_list.clear()
	for i in range(len(new_list)):
		old_list.append(new_list[i])
	new_list.clear()
	time.sleep(1)

# Принято
