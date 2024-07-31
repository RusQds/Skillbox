import os
def save_file(file_path, text):
    open_file = open(file_path, 'w')
    open_file.write(text)
    open_file.close()

def search_file(path, file_name, text):
    if os.path.exists(path):
        file_name = f'{file_name}.txt'
        file_path = os.path.join(path, file_name)
        if os.path.exists(file_path):
            command = input('Вы действительно хотите перезаписать файл? (да/нет) ')
            if command.lower() == 'нет':
                print('Файл не сохранен!')
                return
            elif command.lower() == 'да':
                save_file(file_path, text)
                print('Файл успешно перезаписан!')
            else:
                print('Команда не распознана!')
                print('Файл не сохранен!')
                return
        else:
            save_file(file_path, text)
            print('Файл успешно сохранён!')
    else:
        print('Такой директории не существует!')

# text = input('Введите строку: ')
text = 'testiruyem'
# my_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n')
text_path = 'Users mzavyalov PycharmProjects Python_Basic Module22 05_save'
# file_name = input('Введите имя файла: ')
file_name = 'test'
my_path = os.path.join('C:', os.path.sep)

for elem in text_path.split():
    my_path = os.path.join(my_path, elem)

search_file(my_path, file_name, text)