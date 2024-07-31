import random

count_stick = int(input('Кол-во палок: '))
count_cast = int(input('Кол-во бросков: '))
stick_list = ['I' for _ in range(count_stick)]
for i in range(count_cast):
    now_cast_list = [random.randint(1,count_stick + 1), random.randint(1,count_stick)]
    print(f'Бросок {i + 1}. Сбиты палки с номера {min(now_cast_list)} по номер {max(now_cast_list)}')
    stick_list = [(elem if (i + 1) not in range(min(now_cast_list), max(now_cast_list) + 1) else '.') for i, elem in enumerate(stick_list)]
print(f'Результат: {''.join(stick_list)}')

