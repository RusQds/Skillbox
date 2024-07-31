import random

class People:

	def __init__(self, name, home, satiety=50):
		self.name = name
		self.satiety = satiety
		self.home = home

	def eat(self):
		self.home.food -= 30
		self.satiety += 30

	def work(self, money=0):
		self.home.money += 10
		self.satiety -= 10

	def play(self):
		self.satiety -= 30

	def shop(self):
		self.home.food += 20
		self.home.money -= 20

class Home:
	def __init__(self, food=50, money=0):
		self.food = food
		self.money = money


def life(people, day):
		number = random.randint(1,6)
		if people.satiety < 20:
			people.eat()
		elif people.home.food < 10:
			people.shop()
		elif people.home.money < 50:
			people.work()
		elif number == 1:
			people.work()
		elif number == 2:
			people.eat()
		else:
			people.play()

		if people.satiety < 0:
			print('{name} умер на {day} день.'.format(name=people.name, day=day))
			return False

home = Home()
people_1 = People('Bob', home)
people_2 = People('Jack', home)

day = 1
for i in range(365):
	print(day)
	p_1 = life(people_1, day)
	p_2 = life(people_2, day)
	if p_1 == False or p_2 == False:
		break
	else:
		day += 1

# Принято
