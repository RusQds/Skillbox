
count_peoples = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ', number, 'человек')
start_member = 0

peoples_list = list(range(1, count_peoples + 1))

while len(peoples_list) != 1:
	print('\nТекущий круг людей:', peoples_list)
	print('Начало счёта с номера', peoples_list[start_member])
	kick = (start_member + number - 1) % len(peoples_list)
	print('Выбывает человек под номером', peoples_list[kick])
	peoples_list.remove(peoples_list[kick])
	start_member = kick % len(peoples_list)

print('\nOстался человек под номером', peoples_list[start_member])

# Принято
