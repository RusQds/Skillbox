vowel_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')

result_list = [sym for sym in text if sym in vowel_list]
print(f'Список гласных букв: {result_list}')
print(f'Длина списка: {len(result_list)}')

