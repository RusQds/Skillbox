class Parent:

	def __init__(self, name, age, child):
		self.name=name
		self.age=age
		try:
			if int(child.age) + 16 <= self.age:
				self.child=child
			else:
				self.child = 'нет'
				raise Exception
		except Exception:
			print('Что то слишком уж взрослый у Вас ребенок!')

	def info(self):
		print('Имя: {name}\nВозраст: {age}\nДети:'.format(
			name=self.name,
			age=self.age,
		), end=' ')
		try:
			self.child.info()
		except:
			print('{}'.format(self.child))

	def calm(self):
		print('\n\t###Успокаиваем###')
		self.child.calm_state = 'спокойный'
		self.child.info()

	def feed(self):
		print('\n\t###Кормим###')
		self.child.state_of_hunger = 'сытый'
		self.child.info()