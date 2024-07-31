import random

first_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
final_list = [max(first_list[i], second_list[i]) for i in range(20)]

print(f'Первая команда: {first_list}')
print(f'Вторая команда: {second_list}')
print(f'Победители тура: {final_list}')