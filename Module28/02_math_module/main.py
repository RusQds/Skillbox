import math


class MyMath:
    """Аналог модуля Math"""

    @classmethod
    def circle_len(cls, radius: float) -> float:
        result = 2 * math.pi * radius
        return result

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        result = math.pi * radius**2
        return result

    @classmethod
    def cube_volume(cls, edge: float) -> float:
        result = edge**3
        return result

    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        result = 4 * math.pi * radius**2
        return result


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(edge=7)
res_4 = MyMath.sphere_sq(radius=8)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
