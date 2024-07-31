video_count = int(input('Кол-во видеокарт: '))
old_list = [input(f'{elem + 1} Видеокарта: ') for elem in range(video_count)]
new_list = [elem for elem in old_list if elem != max(old_list)]
print(f'Старый список видеокарт: {old_list}')
print(f'Новый список видеокарт {new_list}')
