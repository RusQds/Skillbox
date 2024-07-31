text = input('Введите текст: ')
text_dict = dict()
text_dict_invert = dict()

for i in text:
	if i in text_dict:
		text_dict[i] += 1
	else:
		text_dict[i] = 1

print('\nОригинальный словарь частот:')
for j in sorted(text_dict.keys()):
	print('{0} - {1}'.format(j, text_dict[j]))

print('\nИнвертированный словарь частот:')
for t in text_dict:
	if text_dict[t] not in text_dict_invert:
		text_dict_invert[text_dict[t]] = [t]
	else:
		text_dict_invert[text_dict[t]].append(t)

for s in sorted(text_dict_invert.keys()):
	print('{0} - {1}'.format(s, text_dict_invert[s]))

# Принято
