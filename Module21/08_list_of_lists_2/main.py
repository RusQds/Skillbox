def normal_list(old_list, new_list):
  for i_elem in old_list:
    if isinstance(i_elem, list):
      normal_list(i_elem, new_list)
    else:
      new_list.append(i_elem)



nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = []

normal_list(nice_list, new_list)
print(new_list)

# Принято
