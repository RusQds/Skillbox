violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
result_list = []
count_music = int(input('Сколько песен выбрать? '))
for i in range(1, count_music + 1):
    music_name = input(f'Название {i} песни: ')
    result_list.extend([violator_songs[i][1] for i in range(len(violator_songs)) if violator_songs[i][0] == music_name])
result = sum(result_list)
print(f'Общее время звучания песен: {result} минут')

