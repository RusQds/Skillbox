import os

alhabet = 'abcdefghijklmnopqrstuvwxyz'
file_name = 'text.txt'
new_file_name = 'analysis2.txt'
sym_dict = dict()
count = 0

print(f'Содержимое файла {file_name}: ')
open_file = open(os.path.abspath(file_name), 'r')
print(open_file.read())
open_file.seek(0)
for sym in open_file.read():
    if sym.lower() in alhabet:
        if sym not in sym_dict:
            sym_dict[sym.lower()] = 1
        else:
            sym_dict[sym.lower()] += 1
        count += 1
open_file.close()

new_file = open(os.path.abspath(new_file_name), 'w')
for key, value in sym_dict.items():
    string = f'{key} {round(value/count, 3)}\n'
    new_file.write(string)
new_file.close()

print(f'Содержимое файла {new_file_name}:')
new_file = open(os.path.abspath(new_file_name), 'r')
print(new_file.read())
new_file.close()
