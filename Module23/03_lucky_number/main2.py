import random

result = 0
try:
    while result < 777:
        number = int(input('Введите число: '))
        random_int = random.randint(1,13)
        if random_int == 13:
            raise Exception
        with open('out_file.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{number}\n')
        result += number
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
except Exception:
    print('Вас постигла неудача!')
    