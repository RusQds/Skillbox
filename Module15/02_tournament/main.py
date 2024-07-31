peoples = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_peoples = []

for i in range(0, len(peoples)):
	if i % 2 == 0:
		new_peoples.append(peoples[i])

print(new_peoples)

# Принято
