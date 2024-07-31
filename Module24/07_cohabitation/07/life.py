class People:
    def __init__(self, name, home):
        self.name = name
        self.hangry = 50
        self.home = home
        self.life = True

    def one_day(self, step):
        if self.hangry < 20 and self.home.get_food() >= 10:
            self.eat()
        elif self.home.get_food() < 10 and self.home.get_money() >= 50:
            self.shop_food()
        elif self.home.get_money() < 50:
            self.work()
        elif step == 1:
            self.work()
        elif step == 2:
            self.eat()
        else:
            self.game()

    def get_info(self):
        print('{}:\nСытость: {}'.format(
            self.name,
            self.hangry
        ))
    def check(self):
        if self.hangry < 0:
            self.life = False

    def eat(self):
        print('{}: Иду есть!'.format(self.name))
        self.hangry += 10
        self.home.set_food(-10)

    def work(self):
        print('{}: Иду работать!'.format(self.name))
        self.home.set_money(10)
        self.hangry -= 10

    def game(self):
        print('{}: Иду играть!'.format(self.name))
        self.hangry -= 10

    def shop_food(self):
        print('{}: Иду в магазин!'.format(self.name))
        self.home.set_food(10)
        self.home.set_money(-10)


class Home:
    def __init__(self):
        self.fridge_food = 50
        self.safe_money = 0

    def get_info(self):
        print('В доме:\nДенег: {}\nЕды: {}'.format(
            self.get_money(),
            self.get_food())
        )
    def set_food(self, food):
        self.fridge_food += food

    def set_money(self, money):
        self.safe_money += money

    def get_food(self):
        return self.fridge_food

    def get_money(self):
        return self.safe_money
