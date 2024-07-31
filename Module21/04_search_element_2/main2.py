def search_value(key_word, search_dict, depth=0, step=1):
    if depth == 0 or (depth > 0 and step <= depth):
        for key, value in search_dict.items():
            if key == key_word:
                return value
            elif isinstance(value, dict):
                result = search_value(key_word, value, depth, step + 1)
                if result:
                    return result

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

key_word = input('Введите искомый ключ: ')
depth_command = input('Хотите ввести максимальную глубину? Y/N:').lower()
if depth_command == 'y':
    depth = int(input('Введите максимальную глубину: '))
    result = search_value(key_word, site, depth)
else:
    result = search_value(key_word, site)
print(result)
