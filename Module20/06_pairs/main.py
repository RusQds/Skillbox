import random

origin_list = [random.randint(0, 10) for i in range(10)]
print('Оригинальный список: {origin}'.format(origin=origin_list))

# 1 способ
new_list = [(origin_list[i], origin_list[i + 1]) for i in range(0, len(origin_list) - 1, 2)]
print('Новый список 1: {new}'.format(new=new_list))

# 2 способ
new_list2 = list()
first_list = list()
second_list = list()
for index_item, object_item in enumerate(origin_list):
	if index_item % 2 == 1:
		second_list.append(object_item)
	else:
		first_list.append(object_item)
new_list2 = zip(first_list, second_list)
print('Новый список 2: {new}'.format(new=list(new_list2)))

# Принято
