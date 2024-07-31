import game
import random

user_1 = game.Unit('Alex', 100)
user_2 = game.Unit('Bob', 100)

my_game = game.Game()

while user_1.point_info() > 0 and user_2.point_info() > 0:
    step = random.randint(0, 1)
    if step == 0:
        my_game.deff(user_1)
    else:
        my_game.deff(user_2)