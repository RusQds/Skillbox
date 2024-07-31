from student import Student
import random

student_names = ['Игорь Иванов', 'Георгий Дудь', 'Алена Михайлова', 'Света Соколова', 'Михаил Шац', 'Ольга Петрова',
				 'Антон Смирнов', 'Илья Ильин', 'Даниил Галкин', 'Артур Пирожков', 'Анна Федорова']

students_list = [Student(people, random.randint(1, 2), [random.randint(1, 5) for _ in range(5)]) for people in student_names ]
new_students_ditc= {item.get_fio(): item.avg_scores() for item in students_list}
new_students_list = sorted(new_students_ditc.values())

for elem in new_students_list:
	for key, value in new_students_ditc.items():
		if elem == value:
			print('{} : {}'.format(key, value))
			student = key
			break
	new_students_ditc.pop(student)