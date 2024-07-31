text = input('Введите текст: ')
start = text.index('h')
stop = (text[::-1].index('h') + 1) * (-1)
reversed_text = text[stop-1:start:-1]
print(reversed_text)

# Принято
