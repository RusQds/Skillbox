site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
#TODO Структура сайта не повторяется, так как имеется общая структура словаря с изменяемыми продуктами, создан список
# активных продуктов.
def print_tree(product, site, line=0):
    for i_elem in site:
        line += 1
        if isinstance(site[i_elem], dict):
            print('\t' * line, '{0} : {{'.format(i_elem))
            print_tree(product, site[i_elem], line=line)
        else:
            if i_elem == 'title' or i_elem == 'h2':
                print('\t' * line, '{0} :'.format(i_elem), str(site[i_elem]).format(product))
            else:
                print('\t' * line, '{0} : {1}'.format(i_elem, (site[i_elem])))
        line -= 1
    print('\t' * line, '}')

def new_site(site, count, activ=list()):
    for i in range(count):
        product = input('Введите название продукта для нового сайта: ')
        activ.append(product)
        for prod in activ:
            print('Сайт для {0}:\nsite = {{'.format(prod))
            print_tree(prod, site)

count = int(input('Сколько сайтов: '))
new_site(site, count)

# Принято
