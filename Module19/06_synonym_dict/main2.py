
count_words = int(input('Введите количество пар слов: '))
words_dict = dict()
for i in range(count_words):
    words_list = input('{} пара: '.format(i + 1)).split(' - ')
    words_dict[words_list[0].lower()] = words_list[1]
    words_dict[words_list[1].lower()] = words_list[0]

while True:
    word = input('Введите слово:')
    if word.lower() in words_dict:
        print('Синоним: {}'.format(words_dict[word]))
        break
    else:
        print('Такого слова в словаре нет.')