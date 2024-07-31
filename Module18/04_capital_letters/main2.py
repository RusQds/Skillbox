text = input('Введите строку: ')
new_text = ' '.join(['{start}{end}'.format(start = word[0].upper(), end = word[1:].lower()) for word in text.split()])
print('Результат: {}'.format(new_text))