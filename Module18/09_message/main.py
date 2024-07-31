simbol_list = list('.,;:/?!#@$%^&*()-=+')
text_list = input('Сообщение: ').split(' ')
new_text_list = []
text_buffer = ''
last_text_buffer = ''

for i in text_list:
    text_buffer = ''
    last_text_buffer = ''
    for j in i:
        if j not in simbol_list:
            text_buffer += j
        else:
            last_text_buffer += text_buffer[::-1]
            last_text_buffer += j
            text_buffer = ''
    last_text_buffer += text_buffer[::-1]
    new_text_list.append(last_text_buffer)

print('Новое сообщение:', ' '.join(new_text_list))

# Принято
