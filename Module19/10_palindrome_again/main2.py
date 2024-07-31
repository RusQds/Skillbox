text = input('Введите строку: ')
text_dict = {sym: text.count(sym) for sym in set(text)}
if [elem % 2 for elem in text_dict.values()].count(1) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
