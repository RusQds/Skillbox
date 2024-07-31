alphabet = 'abcdefg'
result_list = [alphabet[:],
               alphabet[::-1],
               alphabet[::2],
               alphabet[1::2],
               alphabet[:1],
               alphabet[:len(alphabet) - 2:-1],
               alphabet[3:4],
               alphabet[len(alphabet) - 3:],
               alphabet[3:5],
               alphabet[4:2: -1]]
for elem in result_list:
    print(elem)
