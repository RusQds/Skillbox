from life import *

home = Home()
first_people = Male('Alex', home)
second_people = Female('Mary', home)
cat = Cat('Murzik', home)
day = 1

print('Нас зовут {male} и {female}, у нас есть кот {cat}, мы попробуем прожить 365 дней!'.format(male=first_people,
                                                                                                 female=second_people,
                                                                                                 cat=cat))

while first_people.get_life() and second_people.get_life() and cat.get_life():
    print('\n######Идет {} день!######'.format(day))
    first_people.get_info()
    second_people.get_info()
    cat.get_info()
    home.get_info()
    print('_'*10)

    home.one_day()

    first_people.one_day()
    first_people.check()

    second_people.one_day()
    second_people.check()

    cat.one_day()
    cat.check()

    if day >= 366 and first_people.get_life() and second_people.get_life() and cat.get_life():
        print('Мы прожили 365 дней и выжили!')
        break
    elif not first_people.get_life():
        print('{}: Я умер на {} день!'.format(first_people, day))
        break
    elif not second_people.get_life():
        print('{}: Я умерла на {} день!'.format(second_people, day))
        break
    elif not cat.get_life():
        print('{}: Я умер на {} день!'.format(cat, day))
        break
    else:
        print('Мы прожили этот день!')
        day += 1

    print('_'*30)
