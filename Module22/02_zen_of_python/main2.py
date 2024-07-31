import os

open_file = open(os.path.abspath('zen.txt'), 'r')
string_list = [string for string in open_file.read().split('\n')]
for string in reversed(string_list):
    print(string)
open_file.close()