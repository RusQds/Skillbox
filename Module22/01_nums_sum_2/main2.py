import os

sum_numbers = 0
import_file = open(os.path.abspath('numbers.txt'), 'r')
for i_string in import_file:
    string_list = i_string.split()
    if len(string_list) > 0:
        sum_numbers += int(string_list[0])
import_file.close()

export_file = open(os.path.abspath('answer2.txt'), 'w')
export_file.write(str(sum_numbers))
export_file.close()


