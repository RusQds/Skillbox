site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def search_key(s_dict, s_key, deep, line=1, flag=None):
	for i_dict in s_dict:
		if i_dict == s_key:
			return s_dict[i_dict]
		elif isinstance(s_dict[i_dict], dict) and line != deep:
			line += 1
			flag = search_key(s_dict[i_dict], s_key, deep,line)
		if flag != None:
			return flag

def deep():
	q = input('Хотите ввести максимальную глубину? Y/N: ')
	if q.lower() == 'y':
		deep = int(input('Введите максимальную глубину: '))
	else:
		deep = 0
	return deep

key = input('Введите искомый ключ: ')
deep = deep()
print('Значение ключа: {fun}'.format(fun=search_key(site, key, deep)))

# Принято
