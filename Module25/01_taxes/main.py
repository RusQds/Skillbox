class Property:
	worth = 0
	def __init__(self, worth):
		self.worth = worth

	def my_nalog(self):
		nalog = self.worth / 1
		self.nalog = nalog

	def need_money(self, money):
		if money >= self.nalog:
			print('Сумма вашего налога равна {nalog} рублей. У Вас достаточно денег для его погашения.'.format(nalog=self.nalog))
		else:
			need = self.nalog - money
			print('Сумма вашего налога равна {nalog} рублей. Вам не хватает {need} рублей для его погашения.'.format(
				nalog=self.nalog, need=need))

class Appartment(Property):
	def __init__(self, worth):
		super().__init__(worth)
		self.my_nalog()

	def my_nalog(self):
		nalog = self.worth / 1000
		self.nalog = nalog

class Car(Property):
	def __init__(self, worth):
		super().__init__(worth)
		self.my_nalog()

	def my_nalog(self):
		nalog = self.worth / 200
		self.nalog = nalog

class CountryHouse(Property):
	def __init__(self, worth):
		super().__init__(worth)
		self.my_nalog()

	def my_nalog(self):
		nalog = self.worth / 500
		self.nalog = nalog

money = int(input('Введите Ваш бюджет: '))
command = int(input('Введите номер категории Вашего имущества (1. Квартира, 2. Машина, 3. Дача): '))
price = int(input('Введите стоимость Вашего имущества: '))
if command == 1:
	object = Appartment(price)
	object.need_money(money)
elif command == 2:
	object = Car(price)
	object.need_money(money)
elif command == 3:
	object = CountryHouse(price)
	object.need_money(money)

# Принято
