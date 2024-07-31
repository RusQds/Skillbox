

class Node:
	def __init__(self, item=None) -> None:
		self.item = item
		self.next_item = None


class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def __str__(self) -> str:
		path = self.head
		string = '['
		while path.item != None:
			string += str(path.item)
			if path.next_item != None:
				string += str(' ')
				path = path.next_item
			else:
				string += str(']')
				break
		return string

	def append(self, item) -> None:
		new_item = Node(item)
		if self.head is None:
			self.head = new_item
			return
		else:
			steck = self.head
			while steck.next_item != None:
				steck = steck.next_item
			else:
				steck.next_item = new_item
				steck = steck.next_item
				steck.item = item

	def get(self, item: int):
		count = 0
		if self.head is None:
			return None
		else:
			steck = self.head
			while item != count:
				if steck.next_item is not None:
					steck = steck.next_item
					count += 1
				else:
					return None
			else:
				return steck.item

	def remove(self, item: int) -> None:
		count = 0
		if self.head is None:
			return None
		elif item == 0:
			self.head = self.head.next_item
		else:
			steck = self.head
			while count != (item - 1):
				steck = steck.next_item
				count += 1
			steck.next_item = steck.next_item.next_item

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

# Принято

