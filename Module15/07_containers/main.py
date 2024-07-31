def control_weight(container):
	if container > 200 or container < 0:
		print('Ошибка ввода веса контейнера! Контейнер должен быть меньше или равен 200')
		flag = False
	else:
		flag = True
	return flag

def warehouse_add():
	count_container = int(input('Кол-во контейнеров: '))
	warehouse = []
	for _ in range(count_container):
		container = int(input('Введите вес контейнера: '))
		if control_weight(container):
			warehouse.append(container)
		else:
			warehouse.clear()
			print('Попробуйте с начала!')
			warehouse_add()
	print(warehouse)
	add_new_container(warehouse)

def add_new_container(warehouse):
	new_container = int(input('\nВведите вес нового контейнера: '))
	if control_weight(new_container):
		for i in range(len(warehouse)):
			if warehouse[i] < new_container:
				print('Номер, куда встанет новый контейнер:', i + 1)
				break
			elif new_container <= min(warehouse):
				print('Номер, куда встанет новый контейнер:', len(warehouse) + 1)
				break
	else:
		print('Попробуйте снова!')
		add_new_container(warehouse)


warehouse_add()

# Принято
