import math

class Circle:
	def __init__(self, x=0, y=0, r=1):
		self.x = x
		self.y = y
		self.r = r

	def print_circle(self):
		print('\nЦентр заданной окружности находится в точке ({x}, {y}), радиус равен {r}'.format(
			x = self.x,
			y = self.y,
			r = self.r
		))

	def square(self):
		S = self.r**2 * math.pi
		return S

	def perimeter(self):
		P = 2 * self.r * math.pi
		return P

	def expansion(self, expansion=1):
		self.r = self.r * expansion
		print('Радиус увеличен в {} раз.'.format(expansion))

	def intersection(self, x2, y2, r2):
		print('\nЦентр второй заданной окружности находится в точке ({x}, {y}), радиус равен {r}'.format(
			x=x2,
			y=y2,
			r=r2
		))
		if self.x == x2 and self.y == y2 and self.r == r2:
			return None
		elif abs(self.x - x2)**2 + abs(self.y - y2)**2 <= (self.r + r2)**2:
			return True
		else:
			return False