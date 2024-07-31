a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
t1 = a.count(5)
a = [elem for elem in a if elem != 5]
a.extend(c)
t2 = a.count(3)

print('Кол-во цифр 5 при первом объединении:', t1)
print('Кол-во цифр 3 при втором объединении:', t2)
print('Итоговый список:', a)