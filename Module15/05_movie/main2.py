films_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
my_film_list = []
while True:
    my_film = input('Введите фильм: ')
    if my_film in films_list:
        my_film_list.append(my_film)
        print(f'Фильм {my_film} добавлен в Вашу коллекцию')
    else:
        print('Данного фильма нет на сайте!')
    flag = input('Желаете добавить еще фильм? (да\нет): ')
    if flag != 'Да' and flag != 'ДА' and flag != 'да':
        break

print(f'Список Вашей коллекции фильмов: {my_film_list}')

