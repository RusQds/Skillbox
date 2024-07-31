

def first_tour():
	open_file = open('first_tour.txt', 'r')
	player_list = open_file.read().split('\n')
	number = 0
	win_dict = dict()
	count = 0
	for i, i_elem in enumerate(player_list):
		if i != 0:
			if int(i_elem.split(' ')[2]) > int(player_list[0]):
				count += 1
				if i_elem.split(' ')[2] in win_dict:
					win_dict[i_elem.split(' ')[2]].append((i_elem.split(' ')[0], i_elem.split(' ')[1]))
				else:
					win_dict[i_elem.split(' ')[2]] = [[i_elem.split(' ')[0], i_elem.split(' ')[1]]]
	open_file = open('second_tour.txt', 'w')
	open_file.write('{0}\n'.format(count))
	open_file.close()
	for i_key, i_value in reversed(sorted(win_dict.items())):
		for j_elem in i_value:
			number += 1
			second_tour(number, i_key, j_elem)

def second_tour(number, key, value):
	open_file = open('second_tour.txt', 'a')
	open_file.write('{number}) {name}. {family} {point}\n'.format(
		number=number,
		name=value[1][0],
		family=value[0],
		point=key
	))
	open_file.close()

first_tour()

# Принято
