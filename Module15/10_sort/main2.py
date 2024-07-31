def sort_list(n_list):
    for i in range(len(n_list) - 1):
        n_list.append(n_list.pop(n_list.index(min(n_list[:len(n_list) - 1 - i]))))
    n_list.append(n_list.pop(0))

n_list = [1, 4, -3, 0, 10]
sort_list(n_list)
print(n_list)