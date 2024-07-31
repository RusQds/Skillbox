class Student:
	def __init__(self, name='None', number=0, point_list=list()):
		self.name = name
		self.number_group = number
		self.point_list = point_list

	def print_student(self):
		print('Фамилия и Имя: {}\nНомер группы: {}\nУспеваемость: {}\n'.format(self.name, self.number_group,
																																					 self.point_list))

	def average_score(self):
		sum = 0
		len = 0
		for i in self.point_list:
			len += 1
			try:
				sum += int(i)
			except TypeError:
				sum += 0
		return round(sum / len, 1)