name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_list = [value for i, value in enumerate(name_list) if i % 2 == 0]
second_list = [value for i, value in enumerate(name_list) if i % 2 == 1]

print(f'Первая команда: {first_list}')
print(f'Вторая команда: {second_list}')