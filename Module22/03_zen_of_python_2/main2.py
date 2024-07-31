import os

def count_sym(text):
    count = 0
    for sym in text:
        if sym.lower() in alhabet:
            count += 1
    return count

def count_word(text):
    new_text = text.split()
    count = len(new_text)
    return count

def count_line(text):
    count = text.split('\n')
    return len(count)

def rare_sym(text):
    sym_dict = dict()
    for sym in text:
        if sym in alhabet and sym not in sym_dict.keys():
            sym_dict[sym] = 1
        elif sym in alhabet:
            sym_dict[sym] += 1

    new_dict = dict()
    for key, value in sym_dict.items():
        if value not in new_dict.keys():
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)

    min_count = min(new_dict.keys())
    return min_count, new_dict[min_count]


alhabet = 'abcdefghijklmnopqrstuvwxyz'

path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
file_open = open(path, 'r')
file_text = file_open.read()

print('Количество букв в файле: {count}'.format(count=count_sym(file_text)))
print('Количество слов в файле: {count}'.format(count=count_word(file_text)))
print('Количество строк в файле: {count}'.format(count=count_line(file_text)))
rare_tuple = rare_sym(file_text)
print('Наиболее редкая буква: {sym} - {count} шт.'.format(sym=' '.join(rare_tuple[1]), count=rare_tuple[0]))

file_open.close()