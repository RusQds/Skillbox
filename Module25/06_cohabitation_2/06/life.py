

class Cat:
    def __init__(self, name, home):
        self.__name = name
        self.__hangry = 30
        self.__home = home
        self.__life = True

    def __str__(self):
        return self.__name

    def get_info(self):
        print('{name}:\nСытость: {hangry}'.format(
            name=self.__str__(),
            hangry=self.__hangry
        ))

    def check(self):
        if self.__hangry < 0:
            self.__life = False

    def get_life(self):
        return self.__life

    def get_home(self):
        return self.__home

    def eat(self):
        print('{}: Я иду есть!'.format(self.__str__()))
        self.__hangry += 20
        self.get_home().set_cat_food(-10)

    def sleep(self):
        print('{}: Я иду спать!'.format(self.__str__()))
        self.__hangry -= 10

    def tear_wallpaper(self):
        print('{}: Я разодрал обои!'.format(self.__str__()))
        self.get_home().set_dirt()
        self.__hangry -= 10

    def one_day(self):
        if self.__hangry < 20 and self.get_home().get_cat_food() >= 10:
            self.eat()
        else:
            self.tear_wallpaper()
        

class People:
    def __init__(self, name, home):
        self.__name = name
        self.__hangry = 30
        self.__happy = 100
        self.__home = home
        self.__life = True

    def __str__(self):
        return self.__name

    def get_info(self):
        print('{name}:\nСытость: {hangry}\nСчастье: {happy}'.format(
            name=self.__str__(),
            hangry=self.get_hangry(),
            happy=self.get_happy()
        ))
        
    def check(self):
        if self.__hangry < 0 or self.__hangry < 10:
            self.__life = False
            return
        if self.__home.get_cat_food() > 90:
            self.__happy -= 10

    def eat(self):
        print('{}: Иду есть!'.format(self.__name))
        self.__hangry += 30
        self.__home.set_food(-30)

    def petting_at(self):
        print('{}: Глажу кота!'.format(self.__name))
        self.__happy += 5
        self.__hangry -= 10

    def set_happy(self, happy):
        self.__happy += happy

    def set_hangry(self, hangry):
        self.__hangry += hangry

    def get_life(self):
        return self.__life

    def get_happy(self):
        return self.__happy

    def get_hangry(self):
        return self.__hangry

    def get_home(self):
        return self.__home




class Male(People):

    def __init__(self, name, home):
        super().__init__(name, home)

    def game(self):
        print('{}: Иду играть!'.format(self.__str__()))
        self.set_happy(20)
        self.set_hangry(-10)

    def work(self):
        print('{}: Иду работать!'.format(self.__str__()))
        self.get_home().set_money(150)
        self.set_hangry(-10)

    def one_day(self):
        if self.get_hangry() < 20 and self.get_home().get_food() >= 30:
            self.eat()
        elif self.get_happy() <= 40:
            self.game()
        else:
            self.work()


class Female(People):

    def __init__(self, name, home):
        super().__init__(name, home)

    def shop_food(self):
        print('{}: Иду в магазин за продуктами!'.format(self.__str__()))
        self.get_home().set_food(60)
        self.get_home().set_cat_food(10)
        self.get_home().set_money(-70)
        self.set_hangry(-10)

    def shop_fur_coat(self):
        print('{}: Иду покупать шубу!'.format(self.__str__()))
        self.get_home().set_money(-350)
        self.set_happy(60)
        self.set_hangry(-10)

    def cleaning(self):
        print('{}: Убираюсь дома!'.format(self.__str__()))
        self.get_home().set_dirt(-100)
        self.set_hangry(-10)

    def one_day(self):
        if self.get_hangry() < 20 and self.get_home().get_food() >= 30:
            self.eat()
        elif (self.get_home().get_food() < 60 or self.get_home().get_cat_food() < 10) and self.get_home().get_money() >= 70:
            self.shop_food()
        elif self.get_home().get_dirt() >= 90:
            self.cleaning()
        elif self.get_happy() <= 40 and self.get_home().get_money() >= 350:
            self.shop_fur_coat()
        else:
            self.petting_at()


class Home:
    def __init__(self):
        self.__fridge_food = 50
        self.__safe_money = 100
        self.__cat_food = 30
        self.__dirt = 0

    def get_info(self):
        print('В доме:\nДенег: {money}\nЕды: {food}\nКошачьей еды: {cat_food}\nГрязи: {dirt}'.format(
            money=self.get_money(),
            food=self.get_food(),
            cat_food=self.get_cat_food(),
            dirt=self.get_dirt()
        ))

    def set_food(self, food):
        self.__fridge_food += food

    def set_money(self, money):
        self.__safe_money += money
        
    def set_cat_food(self, cat_food):
        self.__cat_food += cat_food
        
    def set_dirt(self, count=5):
        self.__dirt += count

    def get_food(self):
        return self.__fridge_food

    def get_money(self):
        return self.__safe_money
    
    def get_cat_food(self):
        return self.__cat_food
    
    def get_dirt(self):
        return self.__dirt

    def one_day(self):
        self.set_dirt()
