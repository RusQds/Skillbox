count_friends = int(input('Кол-во друзей: '))
count_check = int(input('Долговых расписок: '))
result_list = [0 for _ in range(count_friends)]

my_list = [[int(input(f'\n{i + 1} расписка\nКому: ')), int(input('От кого:')), int(input('Сколько:'))] for i in range(count_check)]
print(my_list)

for n in range(1, count_friends + 1):
    for elem in my_list:
        if elem[0] == n:
            result_list[n - 1] -= elem[2]
        if elem[1] == n:
            result_list[n - 1] += elem[2]


print(f'Баланс друзей:')
for i, value in enumerate((result_list)):
    print(f'{i + 1} : {value}')