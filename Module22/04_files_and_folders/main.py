import os

def file_weight(path, weight=0):
	for j_elem in os.listdir(path):
		new_path = os.path.join(path, j_elem)
		if os.path.isdir(new_path):
			weight += file_weight(new_path)
		else:
			weight += os.path.getsize(new_path)
	return weight

def file_count(path, dirs=0, files=0, weight=0):
	for i_elem in os.listdir(path):
		if os.path.isdir(os.path.join(path, i_elem)):
			dirs += 1
			new_path = os.path.join(path, i_elem)
			weight += file_weight(new_path)
		else:
			files += 1
	print('Размер каталога (в Кб): {0}'.format(weight / 1024))
	print('Количество подкаталогов: {0}'.format(dirs))
	print('Количество файлов: {0}'.format(files))

#path_file = input('Пожалуйста, введите путь до директории: ')
path_file = os.path.abspath(os.path.join('..', '..'))
print(path_file)
file_count(path_file)

# Принято
