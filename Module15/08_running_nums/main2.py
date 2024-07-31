import time

n_list = ['H','E','L','L','O',' ','W','O','R','L','D','!',' ']
k = int(input('Сдвиг: '))
new_list = n_list[:]
print(f'Изначальный список: {''.join(n_list)}')
for i in range(k):
    new_list = [new_list[elem] for elem in range(-1,len(new_list) - 1)]
    print(f'Сдвинутый на {i + 1} элемент список: {''.join(new_list)}')
    time.sleep(1)