zen_python = open('zen.txt', 'r')
zen_list = [i_string for i_string in zen_python.read().split('\n')]
zen_python.close()

for j_string in reversed(zen_list):
	print(j_string)

# Принято
