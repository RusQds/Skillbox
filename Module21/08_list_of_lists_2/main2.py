def ole_line(old_list, new_list=[]):
    for i in old_list:
        if isinstance(i, list):
            ole_line(i)
        else:
            new_list.append(i)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


new_list = ole_line(nice_list)
print(new_list)
