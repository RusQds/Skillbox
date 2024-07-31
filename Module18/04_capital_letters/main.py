
text_list = input('Введите строку: ').split()
new_text_list =[''.join([i[0].upper(), i[1::].lower()]) for i in text_list]
new_text = ' '.join(new_text_list)
print(new_text)

# Принято
