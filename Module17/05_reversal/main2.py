text = input('Введите текст: ')
index_1 = text[:].index('h')
index_2 = text[::-1].index('h')
result = text[len(text) - 2 - index_2: index_1: -1]
print(result)