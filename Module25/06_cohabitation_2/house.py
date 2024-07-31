class House:
	__food = 50
	__cat_food = 30
	__money = 100
	__dirt = 0

	def info(self):
		print('В доме:\nЕды - {food}\nКошачьей еды - {cat_food}\nДенег - {money}\nГряди - {dirt}\n'.format(
			food=self.__food,
			cat_food=self.__cat_food,
			money=self.__money,
			dirt=self.__dirt
		))

	def set_food(self, count):
		self.__food += count

	def get_food(self):
		return self.__food

	def set_cat_food(self, count):
		self.__cat_food += count

	def get_cat_food(self):
		return self.__cat_food

	def set_money(self, count):
		self.__money += count

	def get_money(self):
		return self.__money

	def set_dirt(self, count):
		self.__dirt += count

	def get_dirt(self):
		return self.__dirt

class Men:
	__satiety = 30
	__happiness = 100

	def __init__(self, name, house):
		self.name = name
		self.house = house

	def get_name(self):
		return self.name

	def get_satiety(self):
		return self.__satiety

	def set_satiety(self, count):
		self.__satiety += count

	def get_happiness(self):
		return self.__happiness

	def set_happiness(self, count):
		self.__happiness += count

	def eat(self):
		self.set_satiety(30)
		self.house.set_food(-30)

	def play(self):
		self.set_satiety(-10)
		self.set_happiness(20)

	def work(self):
		self.set_satiety(-10)
		self.house.set_money(150)

	def my_cat(self):
		self.set_satiety(-10)
		self.set_happiness(5)

class Women:
	__satiety = 30
	__happiness = 100

	def __init__(self, name, house):
		self.name = name
		self.house = house

	def get_name(self):
		return self.name

	def get_satiety(self):
		return self.__satiety

	def set_satiety(self, count):
		self.__satiety += count

	def get_happiness(self):
		return self.__happiness

	def set_happiness(self, count):
		self.__happiness += count

	def eat(self):
		self.set_satiety(30)
		self.house.set_food(-30)

	def bay_food(self):
		self.set_satiety(-10)
		self.house.set_money(-100)
		self.house.set_food(100)

	def bay_cat_food(self):
		self.set_satiety(-10)
		self.house.set_money(-50)
		self.house.set_cat_food(50)

	def bay_shuba(self):
		self.set_satiety(-10)
		self.house.set_money(-350)
		self.set_happiness(60)

	def clean(self):
		self.set_satiety(-10)
		self.house.set_dirt(-100)

	def my_cat(self):
		self.set_satiety(-10)
		self.set_happiness(5)

class Cat:
	__satiety = 30

	def __init__(self, name, house):
		self.name = name
		self.house = house

	def get_name(self):
		return self.name

	def get_satiety(self):
		return self.__satiety

	def set_satiety(self, count):
		self.__satiety += count

	def eat(self):
		self.set_satiety(20)
		self.house.set_cat_food(-10)

	def sleep(self):
		self.set_satiety(-10)

	def tear(self):
		self.set_satiety(-10)
		self.house.set_dirt(5)



