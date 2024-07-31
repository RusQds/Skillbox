import os
import zipfile

def result_file(path, result_dict, count_sym):
    with open(path, 'w', encoding='utf-8') as result_file:
        for key in reversed(sorted(result_dict)):
            for elem in result_dict[key]:
                stat = round(key / count_sym, 5)
                result_file.write(f'{elem} - {stat}\n')

def sym_list(path):
    with open(path, 'r', encoding='utf-8') as text_file:
        text_list = [sym.lower() for sym in text_file.read() if sym not in marks]
        return text_list

def count_sym(path, count_dict={}, result_dict={}):
    text_list = sym_list(path)
    count_sym = len(text_list)
    for sym in text_list:
        if sym in count_dict.keys():
            count_dict[sym] += 1
        else:
            count_dict[sym] = 1

    for key, value in count_dict.items():
        if value in count_dict.keys():
            result_dict[value].append(key)
        else:
            result_dict[value] = [key]

    new_file_path = os.path.abspath('result_file.txt')
    result_file(new_file_path, result_dict, count_sym)

def zip_pack(path):
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall()

marks = ' !.,;:\'\"?%* \n-_=+– (){}[]…«»“„`—&/°№'

zip_path = os.path.abspath('voyna-i-mir.zip')
zip_pack(zip_path)

path = os.path.abspath('voyna-i-mir.txt')
print(path)
count_sym(path)
