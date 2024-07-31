def errors_log(string):
	with open('errors.log', 'a', encoding='utf-8') as errors:
		errors.write('Ошибка длинны имени. В строке {} меньше 3х символов\n'.format(string))

string = 0
sym_count = 0
with open('people.txt', 'r') as people_name:
	for i_name in people_name:
		try:
			string += 1
			len_string = len(i_name)
			if i_name.endswith('\n'):
				len_string -= 1
			if len_string < 3:
				raise BaseException
			else:
				sym_count += len_string
		except BaseException:
			print('Ошибка длинны имени. В строке {} меньше 3х символов'.format(string))
			errors_log(string)
	print('Общая длинна символов в файле {}'.format(sym_count))

# Принято
