while True:
	new_file = input('Название файла: ')
	if not new_file.endswith('.txt') and not new_file.endswith('.docx'):
		print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
	elif new_file.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
		print('Ошибка: название начинается на один из специальных символов')
	else:
		print('Файл назван верно.')

# Принято
