import random
class Card:
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']

	def get_card(self):
		if len(self.cards) != 0:
			number = random.randint(0, len(self.cards) -1)
			card = self.cards[number]
			self.cards.remove(self.cards[number])
			return card
		else:
			return None
