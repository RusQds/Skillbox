import os

def count_sym(file, sym_dict=dict(), count_sym={}):
	alhabet = 'abcdefghijklmnopqrstuvwxyz'
	for i in file:
		# TODO Если буква заглавная, то она у вас не посчитается, потому что ее нет в alhabet
		if i in alhabet:
			if i.lower() in sym_dict:
				sym_dict[i.lower()] += 1
			else:
				sym_dict[i.lower()] = 1
	for i_elem, count in sym_dict.items():
		if count in count_sym:
			count_sym[count].append(i_elem)
		else:
			count_sym[count] = [i_elem]
	return count_sym[min(count_sym.keys())]


def split_file(path):
	my_file = open(path, 'r')
	r_file = my_file.read()
	print('Количество букв в файле:', len(list(''.join(r_file.split(' ')))))
	print('Количество слов в файле:', len(' '.join(r_file.split('\n')).split(' ')))
	print('Количество строк в файле:', len(r_file.split('\n')))
	print('Наиболее редкая буква:', count_sym(list(''.join(r_file.split(' ')))))


def search_file(start, file_name):
	for i_elem in os.listdir(start):
		new_path = os.path.join(start, i_elem)
		if i_elem == file_name:
			return new_path
		elif os.path.isdir(new_path):
			file_path = search_file(new_path, file_name)
			if file_path:
				break
	else:
		file_path = None
	return file_path

file_name = 'zen.txt'
start = os.path.abspath(os.path.join('..', '..'))
link = search_file(start, file_name)

split_file(link)

# Принято
