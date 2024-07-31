import card
import blackjack

diller_cards = []
player_cards = []

for _ in range(2):
	diller_cards.append(card.Card().get_card())
	player_cards.append(card.Card().get_card())

while True:
	print('Оставшиеся карты в колоде - {}'.format(card.Card().cards))
	print('Список моих карт - {}'.format(player_cards))
	point_d = blackjack.Blackjack().check(diller_cards)
	point_p = blackjack.Blackjack().check(player_cards)
	if point_d == 21 or point_p == 21 or point_p > 21:
		blackjack.Blackjack().win(point_p, point_d)
		break
	else:
		command = input('Желаете взять еще карту? (да/нет): ')
		if command.lower() == 'да':
			player_cards.append(card.Card().get_card())
		else:
			blackjack.Blackjack().win(point_p, point_d)
			break

# Принято
