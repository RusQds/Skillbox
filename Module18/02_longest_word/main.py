text = input('Введите текст: ').split()
word_count = [len(i) for i in text]

print('Самое длинное слово - ', text[word_count.index(max(word_count))])
print('Его длинна - ', max(word_count))

# Принято
