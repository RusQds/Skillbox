#TODO Разобрался с данной проблемой. Заместо encoding было написано encodingS и программа выдавала ошибку.

import zipfile

def open_zip():
	zip_file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
	zip_file.extractall()
	zip_file.close()

def write_file(dict, count):
	# TODO При записи нужно указать кодировку
	open_file = open('stat.txt', 'w', encoding='utf-8')
	for i in reversed(sorted(dict)):
		for j in sorted(dict[i]):
			open_file.write('{0} - {1}\n'.format(j, round(int(i) / count, 5)))
	open_file.close()

def analys():
	count = 0
	marks = '!.,;:\'\"?%* \n-_=+– (){}[]…«»“„`—&/°№'
	sym_dict = dict()
	new_sym_dict = dict()
	open_zip()
	open_file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
	file_list = ''.join(open_file.read().split(' '))
	for i_sym in file_list:
		if i_sym not in marks:
			if i_sym.lower() not in sym_dict:
				sym_dict[i_sym.lower()] = 1
			else:
				sym_dict[i_sym.lower()] += 1
	for i_sym, i_count in sym_dict.items():
		count += int(i_count)
		if i_count not in new_sym_dict:
			new_sym_dict[i_count] = [i_sym]
		else:
			new_sym_dict[i_count].append(i_sym)

	write_file(new_sym_dict, count)

analys()

# Принято
