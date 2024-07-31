
pizza_dict = dict()
count = int(input('Введите кол-во заказов: '))

#test
# count = 6
# orders_list = ['Иванов Пепперони 1', 'Петров Де-Люкс 2', 'Иванов Мясная 3', 'Иванов Мексиканская 2',
# 							 'Иванов Пепперони 2', 'Петров Интересная 5']

for i in range(count):
	order_list = input('{0} заказ: '.format(i + 1)).split()
	# order_list = orders_list[i].split()
	if order_list[0] not in pizza_dict:
		pizza_dict[order_list[0]] = {order_list[1]: int(order_list[2])}
	# TODO вместо else: if можно написать elif, избавитесь от вложенности
	else:
		if order_list[1] in pizza_dict[order_list[0]]:
			pizza_dict[order_list[0]][order_list[1]] += int(order_list[2])
		else:
			pizza_dict[order_list[0]].update({order_list[1]: int(order_list[2])})

for j in pizza_dict:
	print('{0}: '.format(j))
	for t in sorted(pizza_dict[j].keys()):
		print('\t\t {0}: {1}'.format(t, pizza_dict[j][t]))

# Принято
