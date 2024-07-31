text_list = input('Введите текст: ').split()
count_list = [len(elem) for elem in text_list]

print('Самое длинное слово - {}'.format(text_list[count_list.index(max(count_list))]))
print('Его длинна - {}'.format(max(count_list)))
