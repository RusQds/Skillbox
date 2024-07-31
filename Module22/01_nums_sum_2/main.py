count = 0
numbers =open('numbers.txt', 'r')
string = numbers.read()
for i_elem in string:
	if i_elem != ' ' and i_elem != '\n':
		count += int(i_elem)
numbers.close()

sum_number = open('answer.txt', 'w')
sum_number.write(str(count))
sum_number.close()

# Принято

