import os

def check_peoples(first_path, second_path):
    win_dict = dict()
    first_file = open(first_path, 'r')
    second_file = open(second_path, 'w')
    first_list = first_file.read().split('\n')
    good_point = first_list[0]
    count = 0
    for elem in first_list[1:]:
        if elem.split()[2] > good_point:
            if elem.split()[2] in win_dict:
                win_dict[elem.split()[2]].append(f'{elem.split()[1][0]}. {elem.split()[0]}')
                count += 1
            else:
                win_dict[elem.split()[2]] = [f'{elem.split()[1][0]}. {elem.split()[0]}']
                count += 1

    second_file.write(f'{count}\n')
    for key in sorted(win_dict.keys()):
        for elem in win_dict[key]:
            new_string = f'{elem} {key}\n'
            second_file.write(new_string)
    second_file.close()
    first_file.close()



first_path = os.path.abspath('first_tour.txt')
second_path = os.path.abspath('second_tour2.txt')

check_peoples(first_path, second_path)