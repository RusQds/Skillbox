import math

class CastomCircle:
    def __init__(self,x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_square(self):
        result = math.pi * self.r**2
        print(result)

    def get_perimeter(self):
        result = 2 * math.pi * self.r
        print(result)

    def set_radius(self, k):
        self.r = self.r * k
        print('Радиус окружности стал: {}'.format(self.r))

    def get_intersection(self, x1, y1):
        if abs(self.x - x1) < self.r * 2 or abs(self.y - y1) < self.r * 2:
            print('Окружности пересекаются!')
            return
        print('Окружности НЕ пересекаются!')
        return