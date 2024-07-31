from life import *
import random

home = Home()
first_people = People('Alex', home)
second_people = People('Mary', home)
day = 1

print('Нас зовут {} и {}, мы попробуем прожить 365 дней!'.format(first_people.name, second_people.name))
while first_people.life and second_people.life:
    print('\n######Идет {} день!######'.format(day))
    first_people.get_info()
    second_people.get_info()
    home.get_info()
    print('_'*10)

    #Alex
    step = random.randint(1, 6)
    first_people.one_day(step)
    first_people.check()

    #Mary
    step = random.randint(1, 6)
    second_people.one_day(step)
    second_people.check()

    if day >= 366 and first_people.life and second_people.life:
        print('Мы прожили 365 дней и выжили!')
        break
    elif not first_people.life:
        print('{}: Я умер на {} день!'.format(first_people.name, day))
        break
    elif not second_people.life:
        print('{}: Я умерла на {} день!'.format(second_people.name, day))
        break
    else:
        print('Мы прожили этот день!')
        day += 1

    print('_'*30)