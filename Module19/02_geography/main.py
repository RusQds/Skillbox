

country_dict = dict()
count_country = int(input('Кол-во стран: '))

for i in range(count_country):
	country = input('{0} страна: '.format(i + 1))
	country_list = country.split()
	for u in range(1, len(country_list)):
		country_dict[country_list[u]] = country_list[0]

for j in range(3):
	city = input('\n{0} город: '.format(j + 1))
	if city in country_dict:
		print('Город {0} расположен в стране {1}.'.format(city, country_dict[city]))
	else:
		print('По городу {0} данных нет.'.format(city))

# Принято
