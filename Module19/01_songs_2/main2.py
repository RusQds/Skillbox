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
time_music = [violator_songs.get(input('Название {0} песни: '.format(i + 1)), dict())
              for i in range(count_music)]

print('Общее время звучания песен: {0}'.format(sum(time_music)))