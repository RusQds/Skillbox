import random


class Life:
    normal_carma = 500
    error_list = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']

    def __init__(self, name):
        self.__days = 1
        self.__name = name
        self.__my_carma = 0

    def set_carma(self, carma):
        self.__my_carma += carma

    def get_carma(self):
        return self.__my_carma

    def set_days(self):
        self.__days += 1

    def get_name(self):
        return self.__name

    def get_days(self):
        return self.__days

    def one_day(self):
        day_carma = 0
        raise_day =  random.randint(1, 10)
        if raise_day == 1:
            error_elem = random.choice(self.error_list)
            self.carma_log(error_elem)
        else:
            day_carma = random.randint(1, 7)
            self.set_carma(day_carma)
        self.get_info(name=self.get_name(),
                      day=self.get_days(),
                      carma=day_carma,
                      total_carma=self.get_carma())
        self.set_days()


    def get_info(self, name, day, carma, total_carma):
        print('Меня зовут {name}\n'
              'Идет {day} день\n'
              'Сегодня я заработал {carma} кармы\n'
              'Итого у меня {total_carma} кармы!'.format(name=name,
                                              day=day,
                                              carma=carma,
                                              total_carma=total_carma))

    def chech_carma(self):
        if self.get_carma() >= Life.normal_carma:
            return False
        else:
            return True

    def carma_log(self, error):
        with open('karma.log', 'a', encoding='utf-8') as f:
            f.write(''.join((str(error), '\n')))


people = Life('Alex')
with open('karma.log', 'w', encoding='utf-8') as f:
    pass
while people.chech_carma():
    people.one_day()