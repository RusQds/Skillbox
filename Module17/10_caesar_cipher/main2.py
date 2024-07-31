alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
my_text = input('Введите сообщение: ')
my_step = int(input('Введите сдвиг: '))
new_text = ''.join([(alphabet[(alphabet.index(elem) + my_step) % len(alphabet)]) if elem in alphabet else ' ' for elem in my_text])
print(new_text)
