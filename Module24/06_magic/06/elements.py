class Water:
    def __init__(self):
        self.name = 'Water'

    def get_info(self):
        print('Класс {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Wind):
            return Storm().get_info()
        elif isinstance(other, Fire):
            return Steam().get_info()
        elif isinstance(other, Eath):
            return Dirt().get_info()
        else:
            return None

class Fire:
    def __init__(self):
        self.name = 'Fire'

    def get_info(self):
        print('Класс {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Eath):
            return Lava().get_info()
        elif isinstance(other, Wind):
            return Light().get_info()
        elif isinstance(other, Water):
            return Steam().get_info()
        else:
            return None

class Eath:
    def __init__(self):
        self.name = 'Eath'

    def get_info(self):
        print('Класс {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt().get_info()
        elif isinstance(other, Fire):
            return Lava().get_info()
        elif isinstance(other, Wind):
            return Dust().get_info()
        else:
            return None

class Wind:
    def __init__(self):
        self.name = 'Wind'

    def get_info(self):
        print('Класс {}'.format(self.name))

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm().get_info()
        elif isinstance(other, Fire):
            return Light().get_info()
        elif isinstance(other, Eath):
            return Dust().get_info()
        else:
            return None

class Storm:
    def __init__(self):
        self.name = 'Storm'

    def get_info(self):
        print('Класс {}'.format(self.name))

class Steam:
    def __init__(self):
        self.name = 'Steam'

    def get_info(self):
        print('Класс {}'.format(self.name))

class Dirt:
    def __init__(self):
        self.name = 'Dirt'

    def get_info(self):
        print('Класс {}'.format(self.name))

class Light:
    def __init__(self):
        self.name = 'Light'

    def get_info(self):
        print('Класс {}'.format(self.name))

class Dust:
    def __init__(self):
        self.name = 'Dust'

    def get_info(self):
        print('Класс {}'.format(self.name))

class Lava:
    def __init__(self):
        self.name = 'Lava'

    def get_info(self):
        print('Класс {}'.format(self.name))