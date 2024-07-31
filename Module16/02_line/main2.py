first_min = 160
first_max = 176
first_step = 2
second_min = 162
second_max = 180
second_step = 3

first_list = [elem for elem in range(first_min, first_max + 1, first_step)]
second_list = [elem for elem in range(second_min, second_max + 1, second_step)]
first_list.extend(second_list)
first_list.sort()
print(first_list)