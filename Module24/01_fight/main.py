import random
import unitgame

player_1 = unitgame.Warrior('Воин_1')
player_2 = unitgame.Warrior('Воин_2')

while True:
	stap = random.randint(1,2)
	if stap == 1:
		flag = unitgame.War().battle(player_1, player_2)
	else:
		flag = unitgame.War().battle(player_2, player_1)
	if flag == False:
		break

# Принято
