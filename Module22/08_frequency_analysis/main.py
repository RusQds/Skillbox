import os

def save_file_analysis(sym_dict, count_sym):
	open_file = open('analysis.txt', 'w')
	for count, sym_list in sym_dict.items():
		for i_item in sorted(sym_list):
			open_file.write('{} {}\n'.format(i_item, round(count / count_sym, 3)))


def analysis():
	alhabet = 'abcdefghijklmnopqrstuvwxyz'
	open_file = open('text.txt')
	sym_dict = dict()
	new_sym_dict = dict()
	count = 0
	for sym in ''.join(open_file.read().split('\n')):
		if sym.lower() in alhabet:
			count += 1
			if sym.lower() in sym_dict:
				sym_dict[sym.lower()] += 1
			else:
				sym_dict[sym.lower()] = 1

	for sym, count_sym in sym_dict.items():
		if count_sym in new_sym_dict:
			new_sym_dict[count_sym].append(sym)
		else:
			new_sym_dict[count_sym] = [sym]
	save_file_analysis(new_sym_dict, count)

analysis()

# Принято
