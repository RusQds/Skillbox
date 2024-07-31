from workers import *

workers_list = [Manager('Bob', 'Petrov', 20),
                Manager('John', 'Johnson', 27),
                Manager('Jane', 'Johnson', 24),
                Agent('Alex','Ivanov',40,100000),
                Agent('Bil','Smirnov',53,250000),
                Agent('Max','Sidorov',16,370000),
                Worker('John','Johnson',34,100),
                Worker('Jane','Zav',14,375),
                Worker('Jili','Smit',18,542),]

for people in workers_list:
    print(people)