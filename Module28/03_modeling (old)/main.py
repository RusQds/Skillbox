import math


class Square:
    """Класс описывающий фигуру Квадрат"""

    def __init__(self, edge_len: float) -> None:
        self.__edge_len = edge_len

    @property
    def edge_len(self) -> float:
        return self.__edge_len

    @edge_len.setter
    def edge_len(self, edge_len: float) -> None:
        self.__edge_len = edge_len

    @property
    def square(self) -> float:
        result = self.__edge_len**2
        return result

    @property
    def perimeter(self) -> float:
        result = self.__edge_len * 4
        return result


class Triangle:
    """Класс описывающий фигуру Треугольник"""

    def __init__(self, footing: float, height: float) -> None:
        self.__footing = footing
        self.__height = height

    @property
    def footing(self) -> float:
        return self.__footing

    @property
    def height(self) -> float:
        return self.__height

    @footing.setter
    def footing(self, footing: float) -> None:
        self.__footing = footing

    @height.setter
    def height(self, height: float) -> None:
        self.__height = height

    @property
    def square(self) -> float:
        result = (self.__footing * self.__height) / 2
        return result

    @property
    def perimeter(self) -> float:
        result = 2 * math.sqrt(self.__height**2 + (self.__footing / 2)**2) + self.__footing
        return result


class Cube(Square):
    """Класс описывающий модель Куба"""
    def __init__(self, edge_len: float) -> None:
        super().__init__(edge_len)
        self.figure_name = "Cube"

    def __str__(self) -> str:
        return self.figure_name

    @property
    def square(self) -> float:
        result = super().square * 6
        return result

    @property
    def perimeter(self) -> float:
        result = super().perimeter * 3
        return result


class Pyramid(Triangle, Square):
    """Класс описывающий модель Пирамиды"""
    def __init__(self, footing: float, height: float) -> None:
        super().__init__(footing, height)
        self.figure_name = "Pyramid"

    def __str__(self) -> str:
        return self.figure_name

    @property
    def square(self) -> float:
        result = super().square * 4 + self.footing**2
        return result

    @property
    def perimeter(self) -> float:
        result = super().perimeter * 2 + self.footing * 2
        return result


first_model = Pyramid(10, 15)
print(first_model)
print(f'Площадь модели - {round(first_model.square, 2)}')
print(f'Периметр модели - {round(first_model.perimeter, 2)}')

second_model = Cube(12)
print(second_model)
print(f'Площадь модели - {round(second_model.square, 2)}')
print(f'Периметр модели - {round(second_model.perimeter, 2)}')
