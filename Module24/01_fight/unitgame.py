class Warrior:
	def __init__(self, name='Воин'):
		self.name = name
		self.hp = 100
	def new_hp(self):
		self.hp -= 20
		return self.hp

class War:
	def battle(self, attack, defense):
			hp = defense.new_hp()
			print('{attack} атаковал {defense}, у {defense} осталось {hp} hp.'.format(
				attack=attack.name,
				defense=defense.name,
				hp=str(hp)
			))
			if hp == 0:
				print('Победу одержал {name}'.format(
					name=attack.name))
				return False