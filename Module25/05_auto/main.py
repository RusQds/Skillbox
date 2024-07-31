import math
class Auto:
	def __init__(self, location=(0,0), angle=0):
		self.location = location
		self.angle = angle

	def move(self, distance):
		x1 = round(self.location[0] + distance * math.cos(math.radians(self.angle)), 0)
		y1 = round(self.location[1] + distance * math.sin(math.radians(self.angle)), 0)
		self.location = (x1, y1)
		self.print_info(distance)

	def turn(self, angle):
		self.angle += angle
		print('Мы повернули на {angle} градусов\n'.format(angle=angle))

	def print_info(self, distance):
		print('Мы проехали - {km} км\nНаша новая точка в системе координат - {location}\n'.format(
			km=distance,
			location=self.location
		))

class Bus(Auto):
	__total_money = 0

	def __init__(self,location, angle, passengers):
		super().__init__(location, angle)
		self.passengers = passengers

	def entrance(self):
		self.passengers += 1
		print('Посадили 1 пасажира.')

	def exit(self):
		if self.passengers > 0:
			self.passengers -= 1
			print('Высадили 1 пасажира.')
		else:
			print('Некого высаживать, автобус пустой.')

	def set_total_money(self, count):
		self.__total_money += count

	def get_total_money(self):
		return self.__total_money

	def move(self, distance):
		x1 = round(self.location[0] + distance * math.cos(math.radians(self.angle)), 0)
		y1 = round(self.location[1] + distance * math.sin(math.radians(self.angle)), 0)
		self.location = (x1, y1)
		money = self.passengers * distance
		self.set_total_money(money)
		self.print_info(distance)

	def print_info(self, distance):
		print('За рейс мы проехали - {km} км\n'
					'Перевезли - {passengers} пасажиров\n'
					'Заработали - {total} рублей.\n'
					'Наша новая точка в системе координат - {location}\n'.format(
			km=distance,
			passengers=self.passengers,
			total=self.get_total_money(),
			location=self.location
		))

print('Едем на машине!!!')
auto = Auto((0,0), 30)
auto.move(50)
auto.turn(180)
auto.move(50)
print('Решили побомбить, пересели на автобус!!!')
bus = Bus((1, 1), 30, 10)
bus.move(100)

# Принято
