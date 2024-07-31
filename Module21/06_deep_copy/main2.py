import copy

def edit_value(site, item_name):
    for key, value in site.items():
        if key == 'title' or key == 'h2':
            site[key] = str(value).format(item = item_name)
        elif isinstance(value, dict):
            edit_value(value, item_name)

def activ_site(site, count, site_dict={}):
    for _ in range(count):
        new_site = copy.deepcopy(site)
        item_name = input('Введите название продукта для нового сайта: ')
        edit_value(new_site, item_name)
        site_dict[item_name] = new_site
        for i_item, item_site in site_dict.items():
            print('Сайт для {item}:\n{item_dict}'.format(item=i_item, item_dict=item_site))


site = {
	'html': {
		'head': {
			'title': 'Куплю/продам {item} недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на {item}',
			'div': 'Купить',
			'p': 'продать'
		}
	}
}


count_site = int(input('Сколько сайтов: '))
activ_site(site, count_site)