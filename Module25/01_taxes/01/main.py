class People:
    def __init__(self, name, money=0, appartment=None, car=None, country_house=None):
        self.__name = name
        self.__money = money
        self.__appartment = appartment
        self.__car = car
        self.__country_house = country_house

    def __str__(self):
        return self.__name

    def tax_count(self):
        result = self.__appartment.tax_count() + self.__car.tax_count() + self.__country_house.tax_count()
        return result

    def get_money(self):
        return self.__money

    def check_balance(self):
        if self.tax_count() <= self.get_money():
            return self.tax_count(), 0
        else:
            return self.tax_count(), self.tax_count()-self.get_money()

    def need_money(self):
        tax_count, need_money = self.check_balance()
        print('Налог на имущество: {tax_count} рублей!\n'
              'Баланс в кармане: {money} рублей!\n'.format(tax_count=tax_count,
                                                           money=self.get_money()))
        if need_money > 0:
            print('Для погашения налога недостаточно {need_money} рублей!'.format(need_money=need_money))
        else:
            print('Достаточно денег для погашения налога!')


class Property:

    def __init__(self, worth):
        self.__worth = worth

    def tax_count(self):
        tax = self.get_worth() * 0
        return tax

    def get_worth(self):
        return self.__worth


class Appartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.001

    def tax_count(self):
        tax = self.get_worth() * self.get_tax()
        return tax

    def get_tax(self):
        return self.__tax


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.005

    def tax_count(self):
        tax = self.get_worth() * self.get_tax()
        return tax

    def get_tax(self):
        return self.__tax


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.002

    def tax_count(self):
        tax = self.get_worth() * self.get_tax()
        return tax

    def get_tax(self):
        return self.__tax


people = People(name='Alex',
                money=10000,
                appartment=Appartment(10000000),
                car=Car(3000000),
                country_house=CountryHouse(5000000))

people.need_money()
