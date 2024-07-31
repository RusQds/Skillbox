# numbers = int(input('Кол-во чисел: '))
# numbers_list = [str(int(input('Число: '))) for _ in range(numbers)]
numbers_list = ['1','2','3','2','1', '3']

print(f'\nПоследовательность: {' '.join(numbers_list)}')
for i in range(len(numbers_list)):
    if numbers_list[i::] == numbers_list[-1:-len(numbers_list) - 1 + i:-1]:
        if i == 0:
            need_number = ''
        else:
            need_number = ' '.join(numbers_list[i - 1::-1])
        print(f'Нужно приписать чисел: {i}')
        print(f'Сами числа: {need_number}')
        break
