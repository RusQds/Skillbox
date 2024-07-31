import random
import student

study = ['Игорь Иванов', 'Георгий Дудь', 'Алена Михайлова', 'Света Соколова', 'Михаил Шац', 'Ольга Петрова',
				 'Антон Смирнов', 'Илья Ильин', 'Даниил Галкин', 'Артур Пирожков', 'Анна Федорова']

students_dict = dict()
for i in range(10):
	student_name = study[i]
	number_group = random.randint(1, 10)
	point = [random.randint(1, 5) for _ in range(5)]
	# student_name = input('Введите фамилию и имя студента через пробел: ')
	# group = input('Введите номер группы: ')
	# point = input('Введите оценки через пробел: '.split(' '))
	new_student = student.Student(student_name, number_group, point)
	score = new_student.average_score()
	if score not in students_dict:
		students_dict[score] = [new_student]
	else:
		students_dict[score].append(new_student)

for i_score, i_student in sorted(students_dict.items()):
	for j_elem in i_student:
		print('Средний балл: {}'.format(i_score))
		student.Student.print_student(j_elem)

# Принято
