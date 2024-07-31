violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_music = int(input('Сколько песен выбрать? '))
music_times = 0

for i in range(count_music):
    song = input('Название ' + str(i + 1) + ' песни: ')
    # TODO Можно избавить от if, если использовать метод get словаря:
    #   music_times += violator_songs.get(song, 0)
    #   Если такой песни в словаре нет, то get вернет 0
    if song in violator_songs:
        music_times += violator_songs[song]

print('Общее время звучания песен:', round(music_times, 2), 'минут')

# Принято
