
def calc_func(list):
    result = 0
    if list.split()[1] not in operand:
        raise ArithmeticError
    else:
        try:
            x, y = int(list.split()[0]), int(list.split()[2])
        except:
            raise TypeError

        try:
            result = eval(''.join(list))
        except:
            raise BaseException
        else:
            return result

operand = '+-*/%//'

with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    operand_list = calc_file.read().split('\n')
    for elem in operand_list:
        try:
            result = calc_func(elem)
        except ArithmeticError:
            print(f'В выражении {elem} неверно указана операция')
        except TypeError:
            print(f'В выражении {elem} неверно указан один или несколько операндов')
        except BaseException:
            print(f'В выражении {elem} произошла непонятная ошибка')
        else:
            print(f'Результат выполнения выражения {elem} = {result}')
