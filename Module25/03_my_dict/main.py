class MyDict(dict):
	def __init__(self, my_dict):
		super().__init__(my_dict)

	def get(self, key):
		if key in self.keys():
			return self[key]
		else:
			return 0

free_dict = {1: 2, 2: 3, 3: 4}
my_dict = MyDict(free_dict)
print(my_dict.keys())
print(my_dict.get(3))

# Принято
