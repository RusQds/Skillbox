from house import Men
from house import Women
from house import Cat
from house import House
from life import Life

house = House()
men = Men('Bob', house)
women = Women('Sendy', house)
cat = Cat('Barsik', house)
life = Life()
for i in range(365):
	day = i + 1
	print('День {day}\n'.format(day=day))
	house.set_dirt(5)
	house.info()
	ob_1 = life.men_life(men, day)
	ob_2 = life.women_life(women, day)
	ob_3 = life.cat_life(cat, day)
	if not all([ob_1, ob_2, ob_3]):
		break
	else:
		if house.get_dirt() > 90:
			men.set_happiness(-10)
			women.set_happiness(-10)

print('Все выжили за год!')

# Принято
