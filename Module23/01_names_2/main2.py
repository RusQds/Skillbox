import os

def error_logs(error_string):
    with open('error_log_file.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(error_string)

def count_sym(path):
    result_count = 0
    with open(path, 'r', encoding='utf-8') as open_file:
        for i, line in enumerate(open_file.read().split('\n')):
            try:
                if len(line) >= 3:
                    result_count += len(line)
                else:
                    raise ValueError
            except ValueError:
                error_string = f'Ошибка длинны имени. В строке {i + 1} меньше 3х символов\n'
                error_logs(error_string)
                print(error_string, end='')
        return result_count

file_name = 'people.txt'
file_path = os.path.abspath(file_name)
result = count_sym(file_path)
print(f'Общая сумма символов в файле: {result}')