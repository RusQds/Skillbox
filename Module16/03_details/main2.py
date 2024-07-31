shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item = input('Название детали: ')
count_item = int(input('Кол-во деталей: '))
result = sum([elem for i, elem in enumerate([shop[i][1] for i in range(len(shop)) if shop[i][0] == item]) if (i + 1) <= count_item])

print(f'Общая стоимость - {result}')