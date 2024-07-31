vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')
vowel_text = [x for x in text if x in vowel]
print('Список гласных букв:', vowel_text)
print('Длина списка:', len(vowel_text))

# Принято


