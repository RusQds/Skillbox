from collections.abc import Iterable
#Вроде реализовал, последовательность выходит та же.
def generator(list: list, n: int) -> Iterable:
	count = 2
	if list == [1, 1]:
		yield list[0]
		yield list[1]
		while count != n + 1:
			Q = list[count - list[count - 1]] + list[count - list[count - 2]]
			list.append(Q)
			yield Q
			count += 1
	else:
		return

def print_gen(gener: Iterable) -> None:
	for i in gener:
		print(i, end=' ')


my_gener = generator([1, 1], 20)
print_gen(my_gener)

# Принято
