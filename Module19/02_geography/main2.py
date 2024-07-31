country_list = [input('{0} страна: '.format(i + 1)) for i in range(int(input('Кол-во стран: ')))]
country_dict = {elem.split()[i]: elem.split()[0] for elem in country_list for i in range(1, len(elem.split()))}

for i in range(3):
    town = input('\n{0} город: '.format(i + 1))
    if town in country_dict.keys():
        print('Город {0} расположен в стране {1}.'.format(town, country_dict[town]))
    else:
        print('По городу {0} данных нет.'.format(town))