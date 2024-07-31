from  collections.abc import Iterable

class Iterator:
	def __init__(self, number: int) -> None:
		self.number = number
		self.count = 0

	def __iter__(self) -> Iterable[int]:
		return self

	def __next__(self) -> int:
		if self.count < self.number:
			self.count += 1
			return self.count ** 2
		else:
			raise StopIteration


def generator(number: int) -> Iterable[int]:
	for i in range(1, number + 1):
		yield i ** 2


number = int(input('Введите число: '))

iter = Iterator(number)
for i_elem in iter:
	print(i_elem)

gener = (i ** 2 for i in range(1, number + 1))
for i in gener:
	print(i)

gener2 = generator(number)
for i in gener2:
	print(i)

# Принято


