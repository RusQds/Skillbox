def new_number(number):
    number_list = [sym for sym in str(number)]
    new_number = float(f'{''.join(number_list[number_list.index('.') - 1::-1])}.{''.join(number_list[-1:number_list.index('.'):-1])}')
    return new_number

f_num = float(input('Введите первое число: '))
s_num = float(input('Введите второе число: '))

f_num = new_number(f_num)
s_num = new_number(s_num)
sum_num = f_num + s_num

print(f'Первое число наоборот: {f_num} \nВторое число наоборот: {s_num} \nСумма: {sum_num}')