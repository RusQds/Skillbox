def polindrom(word):
	word_list = {sym: word.count(sym) for sym in {sym for sym in word}}
	count = 0
	for sym in word_list .values():
		if sym % 2 == 1:
			count += 1
	if count > 1:
		return False
	else:
		return True

word = input('Введите строку:')

if polindrom(word):
	print('Можно сделать палиндромом')
else:
	print('Нельзя сделать палиндромом')
