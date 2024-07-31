class Garden:
    def __init__(self, count):
        self.potato_garden = [PotatoGarden(i) for i in range(count)]

    def get_info(self):
        for elem in self.potato_garden:
            elem.get_info()


class PotatoGarden:
    status = ['Посажена', 'Ростки', 'Зеленая', 'Созрела']

    def __init__(self, i):
        self.status = 0
        self.i = i

    def get_info(self):
        if self.status <= 3:
            print('Грядка {} в стадии {}'.format(self.i + 1, PotatoGarden.status[self.status]))
        else:
            print('Картошка уже созрела, давай собирай!')

    def set_status(self):
        if self.status <= 3:
            self.status += 1

class GardenMan:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def get_info(self):
        print('Hello, my name is {}\nУ меня {} грядок'.format(self.name, len(self.garden.potato_garden)))
    def set_potato_status(self):
        print('\n')
        for i in self.garden.potato_garden:
            i.set_status()
            i.get_info()

    def get_potato(self):
        result = 0
        for _ in self.garden.potato_garden:
            result += 100
        self.garden.potato_garden = []
        return result

    def get_info_value_potato(self):
        print('\nВ этом году я собрал {} кг картошки'.format(self.get_potato()))