text = input('Введите слово: ')
uniq_set = set(text)
uniq_count = len([sym for sym in uniq_set if list(text).count(sym) == 1])
print(f'Кол-во уникальных букв: {uniq_count}')