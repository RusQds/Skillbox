

def save_registrations_good(string):
	with open('registrations_good2.log', 'a', encoding='utf-8') as file:
		file.write('{}\n'.format(string))

def save_registrations_bad(string, error):
	with open('registrations_bad2.log', 'a', encoding='utf-8') as file:
		file.write('{0} - Ошибка {1}\n'.format(string, error))

def validate_list(list:list):
    if len(list) != 3:
        raise IndexError
    elif not str(list[0]).isalpha():
        raise NameError
    elif '@' not in list[1] and '.' not in list[1] and list[1].count('@') != 1:
        raise SyntaxError
    elif not isinstance(int(list[2]), int):
        raise ValueError
    elif int(list[2]) not in range(10,100):
        raise ValueError

def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as read_file:
        read_list = read_file.read().split('\n')
        read_list = [elem.split() for elem in read_list]

    for elem in read_list:
        try:
            validate_list(elem)
            save_registrations_good(' '.join(elem))
        except IndexError:
            save_registrations_bad(' '.join(elem), 'IndexError - НЕ присутствуют все три поля')
        except NameError:
            save_registrations_bad(' '.join(elem), 'NameError - поле имени содержит НЕ только буквы')
        except SyntaxError:
            save_registrations_bad(' '.join(elem), 'SyntaxError - Поле емейл НЕ содержит @ и .(точку)')
        except ValueError:
            save_registrations_bad(' '.join(elem), 'ValueError - Поле возраст НЕ является числом от 10 до 99')
    print('Обработка записей завершена')



file_name = 'registrations.txt'
open_file(file_name)
