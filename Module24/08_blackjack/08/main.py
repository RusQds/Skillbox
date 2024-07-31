from game import *

first_player = Player('Alex')
second_player = Player('Bob')

while True:
    game = Game(first_player, second_player)
    game.start_game()
    first_player.get_info()
    second_player.get_info()
    game.next_step()
    game.check()
    game.next_game()