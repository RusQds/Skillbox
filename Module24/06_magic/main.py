class Water:
    def __init__(self):
        self.name = 'water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

class Air:
    def __init__(self):
        self.name = 'air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Fire:
    def __init__(self):
        self.name = 'fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        else:
            return None

class Earth:
    def __init__(self):
        self.name = 'earth'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        else:
            return None

class Storm:
    def __init__(self):
        self.name = 'storm'

class Steam:
    def __init__(self):
        self.name = 'steam'

class Dirt:
    def __init__(self):
        self.name = 'dirt'

class Lightning:
    def __init__(self):
        self.name = 'lightning'

class Dust:
    def __init__(self):
        self.name = 'dust'

class Lava:
    def __init__(self):
        self.name = 'lava'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
storm = water + air
steam = water + fire
dirt = water + earth
lightning = air + fire
dust = air + earth
lava = fire + earth
other = water + storm

print(storm)
print(steam)
print(dirt)
print(lightning)
print(dust)
print(lava)
print(other)

#TODO На сколько смог понять, вроде реализовал. При сложении элементов которые не могут складываться, возвращает
# None. В других случаях позвращает экземпляр класса.

# Принято
