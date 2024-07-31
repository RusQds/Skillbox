# text = input('Введите текст: ')
text = 'Здесь что-то написано'
uniq_set = set(list(text))
sym_dict = {sym: text.count(sym) for sym in uniq_set}
new_dict = dict()
for key, count in sym_dict.items():
    if count in new_dict:
        new_dict[count].append(key)
    else:
        new_dict[count] = [key]

for sym, count in sorted(sym_dict.items()):
    print('{0} : {1}'.format(sym, count))

print()

for sym, count in sorted(new_dict.items()):
    print('{0} : {1}'.format(sym, sorted(count)))