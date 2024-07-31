first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')

for i in range(len(first_text) + 1):
    if i == len(first_text):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        break
    elif '{0}{1}'.format(first_text[i:], first_text[:i]) == second_text:
        print('Первая строка получается из второй со сдвигом {}.'.format(i))
        break