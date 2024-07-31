from person import Manager
from person import Agent
from person import Worker


person_1 = Manager('Jack', 'Petrov', 18)
person_2 = Manager('Poll', 'Ivanov', 28)
person_3 = Manager('Piter', 'Sidorov', 32)
person_4 = Agent('Bob', 'Smirnov', 19)
person_5 = Agent('Alex', 'Sokolov', 50)
person_6 = Agent('Max', 'Andreev', 34)
person_7 = Worker('Jon', 'Vasilyev', 49)
person_8 = Worker('Sendy', 'Orlov', 19)
person_9 = Worker('Ray', 'Grachev', 22)

person_1.print_salary()
person_2.print_salary()
person_3.print_salary()
person_4.print_salary(100000)
person_5.print_salary(325000)
person_6.print_salary(222000)
person_7.print_salary(80)
person_8.print_salary(44)
person_9.print_salary(120)

# Принято
