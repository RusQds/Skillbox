count_people = int(input('Кол-во человек: '))
number_break = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number_break} человек')

people_list = list(range(1, count_people + 1))
start_index = 1
while len(people_list) > 1:
    print(f'\nТекущий круг людей: {people_list}')
    print(f'Начало счёта с номера {people_list[start_index - 1]}')
    last_index = (start_index + number_break - 1) % len(people_list)
    drop_people = people_list.pop(last_index - 1)
    start_index = last_index
    print(f'Выбывает человек под номером {drop_people}')
