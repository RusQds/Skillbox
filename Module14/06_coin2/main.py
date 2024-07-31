
def money(x, y, radius):
	if (x ** 2 + y ** 2) ** 0.5 <= radius:
		print("Монетка где-то рядом")
	else:
		print("Монетки в области нет")


print('Введите координаты монетки:')
x = float(input('X: '))
y =  float(input('Y: '))
radius = int(input('Введите радиус:'))

money(x, y, radius)

# Принято
