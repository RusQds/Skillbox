class Potato:
	def __init__(self, number, maturity):
		self.number=number
		self.maturity=maturity

	def ripeness(self, name):
		if self.maturity == 1:
			stady = 'Посажена'
		elif self.maturity == 2:
			stady = 'Проросла'
		elif self.maturity == 3:
			stady = 'Растет'
		elif self.maturity == 4:
			stady = 'Созрела'
		print('Куст {name} {number} в стадии - {maturity}'.format(
			name=name,
			number=self.number,
			maturity=stady
		))
		return stady

class Garden:
	def __init__(self, name):
		self.name = name

	def garden_bed(self, count):
		for i in range(1, 5):
			garden_bed_list = list()
			for j in range(1, count + 1):
				bush = Potato(j, i)
				garden_bed_list.append(bush)
				stady = bush.ripeness(self.name)
			print()
		if stady == 'Созрела':
			print('Можно собирать урожай')
			return count

class Gardener:
	def __init__(self, name, garden):
		self.name=name
		self.garden_bed=garden

	def care(self, count):
		Garden(self.garden_bed).garden_bed(count)
		print()
		return count

	def harvest(self, count, list=[]):
		for i in range(count):
			list.append(1)
		print('{name} собрал {count} кустов картошки'.format(name=self.name, count=count))

my_gardener = Gardener('Bob', 'Картошка')

my_gardener.harvest(my_gardener.care(3))

# Принято
