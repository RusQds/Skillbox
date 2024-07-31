def weight_control(weight):
    if weight > 200:
        print('Слишком тяжелый, этот везем на другой склад!')
        return 0
    return weight
def next_box():
    next_box = int(input('Введите вес контейнера: '))
    return weight_control(next_box)

count_box = int(input('Кол-во контейнеров: '))
box_list = [elem for elem in [next_box() for _ in range(count_box)] if elem != 0]

new_box = int(input('Введите вес нового контейнера: '))
new_box = weight_control(new_box)
index_box = 0
if new_box == 0:
    index_box = -1
else:
    for key, value in enumerate(box_list):
        if value < new_box:
            index_box = key + 1
            break
print(f'Номер, куда встанет новый контейнер: {index_box}')

