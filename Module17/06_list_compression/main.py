import random
import math

def generator_numbers():
	number = math.floor(random.randint(0,9) * random.random())
	return number

numbers_list = [generator_numbers() for _ in range(random.randint(1, 21))]
print(numbers_list)

for i in numbers_list:
	if i == 0:
		numbers_list.append(numbers_list.pop(numbers_list.index(0)))
print(numbers_list)

for j in range(numbers_list.count(0)):
	numbers_list.remove(0)
print(numbers_list)

# Принято
