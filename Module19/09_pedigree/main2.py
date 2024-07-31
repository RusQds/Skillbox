def parent_fanc(start_list, d_dict):
    for elem in start_list:
        if elem not in d_dict:
            d_dict[elem] = {}
            child_fanc(elem, d_dict[elem])
def child_fanc(name, e_dict):
    if len(p_list) == 0:
        lvl = -1
        iter_dict(lvl, d_dict, result_dict)
        return
    for elem in p_list[:]:
        parent = elem.split()[1]
        if parent == name:
            child = elem.split()[0]
            e_dict[child] = {}
            p_list.remove(elem)
            child_fanc(child, e_dict[child])
def iter_dict(lvl, i_dict: dict, f_dict: dict):
    if len(i_dict) == 0:
        return
    lvl += 1
    for i in i_dict.keys():
        f_dict[i] = lvl
        print('{0} - {1}'.format(i, lvl))
        iter_dict(lvl, i_dict[i], f_dict)

p_list = ['Alexei Peter_I', 'Anna Peter_I', 'Elizabeth Peter_I', 'Peter_II Alexei', 'Peter_III Anna', 'Paul_I Peter_III', 'Alexander_I Paul_I', 'Nicholaus_I Paul_I']
perent_list = [elem.split()[1] for elem in p_list]
child_list = [elem.split()[0] for elem in p_list]
start_list = list(set(perent_list).difference(child_list))
d_dict = dict()
result_dict = dict()

print('“Высота” каждого члена семьи:')
parent_fanc(start_list, d_dict)

