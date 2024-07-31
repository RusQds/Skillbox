class Blackjack:
	def check(self, cards):
		point = 0
		for i_elem in cards:
			if i_elem == 'V' or i_elem == 'D' or i_elem == 'K':
				point += 10
			elif i_elem == 'T':
				# TODO 11 - пока общая сумма не больше 21, а не 10
				# Реализовал из своих знаний данной игры=) Когда играли в данную игру, можно было представлять ее и как 11 и
				# как 1. То есть если у меня 20 и я получаю туза, он может быть единицей и тогда у меня 21. Надеюсь это не
				# так принципиально для зачета задания=)
				if point <= 10:
					point += 11
				else:
					point += 1
			else:
				point += int(i_elem)
		return point

	def win(self, point_p, point_d):
		print('Игрок - {}, Диллер - {}.'.format(point_p, point_d), end=' ')
		if point_p > 21 and point_d > 21:
			print('Победителя нет.')
		elif point_d > 21:
			print('Игрок победил.')
		elif point_p > 21:
			print('Диллер победил.')
		elif point_d == point_p:
			print('Ничья')
		elif point_d > point_p:
			print('Диллер победил.')
		elif point_p > point_d:
			print('Игрок победил.')