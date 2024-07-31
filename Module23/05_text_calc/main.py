def calc(calc_list):
	operators = ['+','-','*','/','%','//']
	if calc_list[1] not in operators:
		raise ArithmeticError
	else:
		try:
			number1, number2 = int(calc_list[0]), int(calc_list[2])
		except:
			raise TypeError
		try:
			result = eval(''.join(calc_list))
			return result
		except:
			raise Exception

sum_result = 0
with open('calc.txt', 'r', encoding='utf-8') as file:
	for i_line in file:
		if i_line.endswith('\n'):
			calc_list = i_line[:i_line.index('\n')].split(' ')
		else:
			calc_list = i_line.split(' ')
		try:
			result = calc(calc_list)
			print('{0} = {1}'.format(' '.join(calc_list), result))
			sum_result += result
		except ArithmeticError:
			print('Выражение {0} не удалось посчитать, операция в выражении задана не правильно.'.format(' '.join(calc_list)))
		except TypeError:
			print('Выражение {0} не удалось посчитать, операнд в выражении задан не правильно.'.format(' '.join(calc_list)))
		except Exception:
			print('Выражение {0} не удалось посчитать, произошла какая то ошибка.'.format(' '.join(calc_list)))
	print('Сумма всех посчитаных выражений = {0}'.format(sum_result))

# Принято
