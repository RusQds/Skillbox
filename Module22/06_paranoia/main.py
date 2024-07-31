import os

def cesar_text(index, text):
	alhabet = 'abcdefghijklmnopqrstuvwxyz'
	new_text_list = []
	for i in text:
		if i in alhabet.lower():
			new_text_list.append(alhabet[(alhabet.index(i.lower()) + index) % (len(alhabet) + 1)])
		elif i in alhabet.upper():
			new_text_list.append(alhabet[(alhabet.index(i.lower()) + index) % (len(alhabet) + 1)].upper())
	new_text = ''.join(new_text_list)
	return new_text

def new_file(list):
	for i_index, i_elem in enumerate(list):
		new_text = cesar_text(i_index + 1, i_elem)
		new_file = open('cipher_text.txt', 'a')
		new_file.write(new_text)
		new_file.write('\n')
		new_file.close()

def open_file():
	open_file = open('text.txt', 'r')
	split_list = open_file.read().split('\n')
	new_file(split_list)
	open_file.close()

open_file()

# Принято
