import os
from collections.abc import Iterable

def gen_files_path(dir: str, path='D:') -> Iterable:
	for i_elem in os.listdir(path):
		new_path = os.path.join(path, i_elem)
		if i_elem == dir:
			print('Дирректория найдена. Путь к ней {}'.format(new_path))
			return new_path
		elif os.path.isfile(new_path):
			yield new_path
		else:
			for i_path in gen_files_path(dir, new_path):
				yield i_path
	return


my_dir = input('Введите название каталога: ')
my_path = 'D:\Games'

files_path = gen_files_path(my_dir, my_path)
for i in files_path:
	print(i)

# Принято
