class Person:
	def __init__(self, name, family, age):
		self.__name = name
		self.__family = family
		self.__age = age

	def print_person(self):
		print('\nName: {name}\nFamily: {family}\nAge: {age}'.format(
			name=self.get_name(),
			family=self.get_family(),
			age=self.get_age()
		))

	def get_name(self):
		return self.__name

	def get_family(self):
		return self.__family

	def get_age(self):
		return self.__age

class Employee(Person):

	def salary(self):
		return  0

	def print_salary(self, count=0):
		self.set_count(count)
		self.print_person()
		print('Зарплата: {salary}'.format(salary=self.salary()))

class Manager(Employee):
	def __init__(self, name, family, age):
		super().__init__(name, family, age)

	def salary(self):
		return 13000

	def set_count(self, count):
		pass

class Agent(Employee):
	__volume_of_sales = 0

	def __init__(self, name, family, age):
		super().__init__(name, family, age)

	def salary(self):
		return 5000 + (self.get_count_of_sales() / 100 * 5)

	def set_count(self, volume_of_sales):
		self.__volume_of_sales = volume_of_sales

	def get_count_of_sales(self):
		return self.__volume_of_sales

class Worker(Employee):
	__work_time = 0

	def __init__(self, name, family, age):
		super().__init__(name, family, age)

	def salary(self):
		return 100 * self.get_work_time()

	def set_count(self, work_time):
		self.__work_time = work_time

	def get_work_time(self):
		return self.__work_time