

class Person:

    def __init__(self, name, lastname, age):
        self.__name = name
        self.__lastname = lastname
        self.__age = 0
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_lasname(self):
        return self.__lastname

    def set_age(self, age):
        if 100 >= age >= 0:
            self.__age = age


class Employee(Person):

    def __init__(self, name, lastname, age):
        super().__init__(name, lastname, age)

    def __str__(self):
        return ('Меня зовут {name}\n'
                'Моя фамилия {lastname}\n'
                'Мне {age} лет\n'
                'Моя зарплата {salary} рублей\n\n').format(
            name=self.get_name(),
            lastname=self.get_lasname(),
            age=self.get_age(),
            salary=self.get_salary())

    def get_salary(self):
        salary = 1000
        return salary


class Manager(Employee):

    def __init__(self, name, lastname, age):
        super().__init__(name, lastname, age)
        self.__salary = 13000

    def get_salary(self):
        return self.__salary


class Agent(Employee):
    def __init__(self, name, lastname, age, amount_sales):
        super().__init__(name, lastname, age)
        self.__salary = 5000
        self.__amount_sales = amount_sales

    def get_salary(self):
        result = self.__salary + self.__amount_sales * 0.05
        return result


class Worker(Employee):

    def __init__(self, name, lastname, age, work_time):
        super().__init__(name, lastname, age)
        self.__bet = 100
        self.__work_time = work_time

    def get_salary(self):
        result = self.__bet * self.__work_time
        return result
