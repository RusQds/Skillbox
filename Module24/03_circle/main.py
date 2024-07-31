import circle

my_circle = circle.Circle()
my_circle.print_circle()
print('Площадь окружности: {}'.format(my_circle.square()))
print('Периметр окружности: {}'.format(my_circle.perimeter()))
my_circle.expansion(3)
my_circle.print_circle()

intersection = my_circle.intersection(0, 3, 1)
if intersection:
	print('Окружности пересекаются')
elif intersection == None:
	print('Точек пересечения бесконечное множество: окружности лежат друг на друге')
else:
	print('Окружности не пересекаются')

# Принято
