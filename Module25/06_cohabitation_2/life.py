import random
from house import Men
from house import Women
from house import Cat

class Life:

	def men_life(self, people, day):
		if people.get_satiety() <= 30 and people.house.get_food() >= 30:
			people.eat()
		elif people.get_happiness() <= 50 and people.get_satiety() > 10:
			people.play()
		elif people.house.get_money() < 100 and people.get_satiety() > 10:
			people.work()
		else:
			people.my_cat()
		return self.check(people, day)


	def women_life(self, people, day):
		if people.get_satiety() <= 30 and people.house.get_food() >= 30:
			people.eat()
		elif people.house.get_money() >= 100 and people.get_satiety() > 10 and people.house.get_food() < 100:
			people.bay_food()
		elif people.house.get_money() >= 50 and people.house.get_cat_food() <= 50:
			people.bay_cat_food()
		elif people.get_happiness() <= 50 and people.get_satiety() > 10 and people.house.get_money() >= 350:
			people.bay_shuba()
		elif people.house.get_dirt() >=90 and people.get_satiety() > 10:
			people.clean()
		else:
			people.my_cat()
		return self.check(people, day)

	def cat_life(self, cat, day):
		number = random.randint(1,2)
		if cat.get_satiety() <= 30 and cat.house.get_cat_food() >= 30:
			cat.eat()
		elif number == 1:
			cat.sleep()
		else:
			cat.tear()
		return self.check(cat, day)

	def check(self, object, day):
		if isinstance(object, Men):
			if object.get_satiety() <= 0 or object.get_happiness() < 10:
				print('{name} умер на {day} день.'.format(name=object.get_name(), day=day))
				return False
			else:
				return True
		else:
			if object.get_satiety() <= 0:
				print('{name} умер на {day} день.'.format(name=object.get_name(), day=day))
				return False
			else:
				return True