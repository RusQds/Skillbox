nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
result_list = [elem3 for elem1 in nice_list for elem2 in elem1 for elem3 in elem2]
print(result_list)