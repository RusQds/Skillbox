students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код

def serch(students, pairs, my_lst):
    l = 0
    for i_student, i_info in students.items():
        pairs.append((i_student, i_info['age']))
        for i_interests in i_info['interests']:
            my_lst.add(i_interests)
        l += len(i_info['surname'])
    return l

pairs = list()
my_lst = set()
serch(students, pairs, my_lst)

print('Список пар "ID студента - Возраст": {0}'.format(pairs),
      '\nПолный список интересов всех студентов: {0}'.format(my_lst),
      '\nОбщая длина всех фамилий студентов: {0}'.format(serch(students, pairs, my_lst)))

# Принято
