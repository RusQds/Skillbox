simbol_list = list('.,;:/?!#@$%^&*()-=+')
my_text = input('Сообщение: ')
new_text_list = []
my_text_list = my_text.split()
for word in my_text_list:
    if word[-1] in simbol_list:
        new_text_list.append('{0}{1}'.format(word[-2::-1], word[-1]))
    else:
        new_text_list.append(word[::-1])
new_text = ' '.join(new_text_list)
print('Новое сообщение: {}'.format(new_text))