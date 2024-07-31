string_cod = 'aaAAbbсaaaA'
count = 1
new_list = []
for i in range(len(string_cod)):
    if i != len(string_cod) - 1:
        if string_cod[i] == string_cod[i + 1]:
            count += 1
        else:
            new_list.append('{elem}{count}'.format(count=count, elem=string_cod[i]))
            count = 1
    else:
        new_list.append('{elem}{count}'.format(count=count, elem=string_cod[i]))
        count = 1

print(''.join(new_list))