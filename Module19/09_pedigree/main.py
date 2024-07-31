count = int(input('Введите количество человек: '))
family_dict = dict()
family_tree_dict = dict()
family_name = list()

for i in range(count - 1):
	line_list = input('{0} пара: '.format(i + 1)).split(' ')
	if line_list[1] not in family_dict:
		family_dict[line_list[1]] = [line_list[0]]
	else:
		family_dict[line_list[1]].append(line_list[0])
	if line_list[0] not in family_name:
		family_name.append(line_list[0])

for name in family_dict.keys():
	if name not in family_name:
		if name not in family_tree_dict:
			family_tree_dict[name] = 0
		for child in family_dict[name]:
			if child not in family_tree_dict:
				family_tree_dict[child] = family_tree_dict[name] + 1
				family_name.remove(child)

print('“Высота” каждого члена семьи:')
for people in sorted(family_tree_dict.keys()):
	print('{} - {}'.format(people, family_tree_dict[people]))

# Принято
