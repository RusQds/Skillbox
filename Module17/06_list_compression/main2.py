import random

n = int(input('Введите длинну списка: '))
nums_list = [random.randint(0, 9) for _ in range(n)]
print(nums_list)
for _ in range(nums_list.count(0)):
        nums_list.append(nums_list.pop(nums_list.index(0)))
print(nums_list)
nums_list = [elem for elem in nums_list[:] if elem != 0]
print(nums_list)