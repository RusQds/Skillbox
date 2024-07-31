def min_len(f_e, s_e):
    m_len = min(len(f_e), len(s_e))
    return m_len

def zip_clone(f_e, s_e, step = 0, r_l=list()):
    if step != 1:
        zip_clone(f_e, s_e, step - 1, r_l)
    r_l.append((list(f_e)[step - 1], list(s_e)[step - 1]))

a = 'sdf'
b = [1, 2, 3, 4, 5]
c = (1, 2, 3, 4, 5)
d = {1, 2, 3, 4, 5, 6}
e = {1: 2, 3: 4, 5: 6}

result = list()
zip_clone(b, e, min_len(b, e), result)
print(result)