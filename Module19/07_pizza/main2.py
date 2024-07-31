
# count_pizza = int(input('Введите кол-во заказов: '))
count_pizza = 6
check_dict = dict()
my_list = ['Иванов Пепперони 1', 'Петров Де-Люкс 2', 'Иванов Мясная 3', 'Иванов Мексиканская 2', 'Иванов Пепперони 2', 'Петров Интересная 5']
for i in range(count_pizza):
    # check_list = input('{0} заказ: '.format(i + 1)).split()
    check_list = my_list[i].split()

    if check_list[0] not in check_dict:
        check_dict[check_list[0]] = {}
        check_dict[check_list[0]][check_list[1]] = int(check_list[2])
    elif check_list[1] not in check_dict[check_list[0]]:
        check_dict[check_list[0]][check_list[1]] = int(check_list[2])
    else:
        check_dict[check_list[0]][check_list[1]] += int(check_list[2])

for key, value in check_dict.items():
    print('{0} :'.format(key))
    for key_2, value_2 in value.items():
        print('........{0} : {1}'.format(key_2, value_2))
