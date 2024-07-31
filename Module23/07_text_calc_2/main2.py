
def calc_func(list):
    result = 0
    try:
        x, y = int(list.split()[0]), int(list.split()[2])
        result = eval(''.join(list))
    except:
        raise BaseException
    else:
        return result

operand = '+-*/%//'

with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    operand_list = calc_file.read().split('\n')
    result = 0
    sum_results = 0
    for elem in operand_list:
        try:
            result = calc_func(elem)
        except BaseException:
            command = input(f'Обнаружена ошибка в строке: {elem}  Хотите исправить?(да\нет) - ')
            if command.lower() == 'да':
                new_string = input('Введите исправленную строку: ')
                try:
                    result = calc_func(new_string)
                except:
                    print('Увы, опять ошибка!')
                else:
                    print(f'Результат выполнения выражения {new_string} = {result}')
                    sum_results += result
        else:
            print(f'Результат выполнения выражения {elem} = {result}')
            sum_results += result
    print(f'Сумма результатов: {sum_results}')