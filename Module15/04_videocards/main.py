count = int(input('Кол-во видеокарт: '))
list_video_cards =[]
new_list_video_cards = []


for i in range(count):
	list_video_cards.append(int(input(str(i + 1) + ' Видеокарта: ')))

max_generation = max(list_video_cards)

for i in list_video_cards:
	if i != max_generation:
		new_list_video_cards.append(i)

print('Старый список видеокарт: ', list_video_cards)
print('Новый список видеокарт: ', new_list_video_cards)

# Принято
