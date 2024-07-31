class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.point = hp

    def point_info(self):
        return self.point

    def blood(self, attac):
        self.point -= attac
        if self.point <= 0:
            print("Игрок {} убит!".format(self.name))
        else:
            print("У игрока {} осталось {} здоровья!".format(self.name, self.point))

class Game:
    def __init__(self):
        self.attac_point = 20

    def deff(self, unit):
        if unit.point_info() > 0:
            unit.blood(self.attac_point)

