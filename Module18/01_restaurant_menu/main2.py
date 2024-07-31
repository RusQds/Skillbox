menu_list = input('Доступное меню: ').split(';')
menu_text = ', '.join(menu_list)
print('На данный момент в меню есть: {text}'.format(text = menu_text))