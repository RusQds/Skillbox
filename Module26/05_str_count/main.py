import os
#Тест

def generator(path: str):
	for i_file in os.listdir(path):
		count = 0
		if os.path.isfile(i_file) and i_file.endswith('.py'):
			with open(i_file, 'r') as file:
				for string in file:
					if not string.startswith('#') and not (string.endswith('\n') and len(string) == 1):
						count += 1
				yield count

my_path = os.path.abspath('')
my_code = generator(my_path)
for i_elem in my_code:
	print(i_elem)

# Принято
