import random
import os

class Game:
    cards = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
    def __init__(self,first_player,second_player):
        self.first_player = first_player
        self.second_player = second_player

    def start_game(self):
        self.first_player.cards = [self.get_card() for _ in range(2)]
        self.second_player.cards = [self.get_card() for _ in range(2)]

    def next_step(self):
        while self.first_player.get_card():
            self.first_player.cards.append(self.get_card())
            self.first_player.get_info()
            if self.sum_points(self.first_player) > 21:
                print('Перебор!')
                break
        while self.second_player.get_card():
            self.second_player.cards.append(self.get_card())
            self.second_player.get_info()
            if self.sum_points(self.second_player) > 21:
                print('Перебор!')
                break

    def next_game(self):
        while True:
            game = input('Сыграем еще? (yes/no): ')
            if game == 'yes':
                return True
            elif game == 'no':
                return False
            else:
                print('Команда не распознана!')

    def get_card(self):
        index = random.randint(0,len(Game.cards)-1)
        card = Game.cards[index]
        Game.cards.pop(index)
        return card

    def sum_points(self, player):
        cards_list = player.cards[:]
        result = 0

        # Подсчет без тузов
        for card in player.cards:
            if card != 'A' and type(card) == int:
                result += card
                cards_list.remove(card)
            elif card != 'A' and card in ['J', 'Q', 'K']:
                result += 10
                cards_list.remove(card)

        # Подсчет по тузам
        for index in range(len(cards_list)):
            if result <= 10 and index == len(cards_list)-1:
                result += 11
            elif (result <= 10 and index != len(cards_list)-1) or (result > 10):
                result += 1
        return result

    def check(self):
        first_result = self.sum_points(self.first_player)
        second_result = self.sum_points(self.second_player)
        if first_result > 21 and second_result > 21:
            print('Оба игрока проиграли!')
        elif (first_result <= 21 and second_result > 21):
            print('Победил игрок {}'.format(self.first_player.name))
        elif first_result > 21 and second_result <= 21:
            print('Победил игрок {}'.format(self.second_player.name))
        elif first_result > second_result:
            print('Победил игрок {}'.format(self.first_player.name))
        elif first_result < second_result:
            print('Победил игрок {}'.format(self.second_player.name))
        else:
            print('Ничья')
        print('Игрок {} - {} очков : Игрок {} - {} очков'.format(self.first_player.name, first_result, self.second_player.name, second_result))

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_info(self):
        print('Карты у игрока {} - {}'.format(self.name, self.cards))

    def get_card(self):
        while True:
            flag = input('{} - Еще карту? (yes/no): '.format(self.name))
            if flag.lower() == 'yes':
                return True
            elif flag.lower() == 'no':
                return False
            else:
                print('Команда не распознана!')