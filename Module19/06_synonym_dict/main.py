def word_search(word_dict, word_dict_invert):
	word_quest = input('Введите слово: ').lower()
	if word_quest in word_dict.keys() or word_quest in word_dict_invert.keys():
		if word_quest in word_dict.keys():
			print('Синоним: {0}'.format(word_dict[word_quest]))
		else:
			print('Синоним: {0}'.format(word_dict_invert[word_quest]))
	else:
		print('Такого слова в словаре нет.')
		word_search(word_dict, word_dict_invert)

count = int(input('Введите количество пар слов: '))
word_dict = dict()
word_dict_invert = dict()

for i in range(count):
	word = input('{0} пара: '.format(i + 1)).lower().replace(' ', '')
	word_dict[word.split('-')[0]] = word.split('-')[1]

for j in word_dict:
	# TODO Можно было использовать тот же словарь word_dict вместо двух словарей
	#  Тогда и функция word_search получилась бы короче
	word_dict_invert[word_dict[j]] = j

word_search(word_dict, word_dict_invert)

# Принято
