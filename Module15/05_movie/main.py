films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
like_list_films = []

def add_films(films, like_list_films):
    film = input('Какой фильм добавить в список избранных? ')

    if film in films:
      like_list_films.append(film)
    else:
      print('Данного фильма нет на сайта.')

    flag = input('Желаете добавить еще фильм? (yes/no)')

    if flag == 'no':
      return like_list_films
    else:
      add_films(films, like_list_films)


add_films(films, like_list_films)
print('Ваш список избранных фильмов', like_list_films)

# Принято
