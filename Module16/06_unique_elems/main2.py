
first_list = [1, 2, 3]
second_list = [2, 4, 6, 3, 3, 2, 1]
first_list.extend(second_list)
first_list = list(set(first_list))
print(f'Новый первый список с уникальными элементами: {first_list}')