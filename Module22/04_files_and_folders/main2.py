import os
def search_dirs(look_path, count_dirs=0, coun_file=0, count_kbit=0):
    if os.path.exists(look_path):
        print('\nСмотрим директорию {path}'.format(path=look_path))
        for i_elem in os.listdir(look_path):
            if os.path.isdir(os.path.join(look_path, i_elem)):
                count_dirs += 1
                count_dirs, coun_file, count_kbit = search_dirs((os.path.join(look_path, i_elem)), count_dirs, coun_file, count_kbit)
            if os.path.isfile(os.path.join(look_path, i_elem)):
                coun_file += 1
                file_weight = os.path.getsize((os.path.join(look_path, i_elem)))
                count_kbit += file_weight
                print('         Найден файл {file_name}, его размер {weight} байт'.format(
                    file_name=os.path.join(look_path, i_elem),
                    weight=file_weight))
    else:
        print('Директории {dir} не существует!'.format(dir=look_path))
        return

    return (count_dirs, coun_file, count_kbit)

# path_dirs = input('Пожалуйста, введите путь до директории: ')
path_dirs = os.path.abspath(os.path.join('..'))

result_tuple = search_dirs(path_dirs)
weight_file = result_tuple[2]/1024/1024
count_dirs = result_tuple[0]
count_file = result_tuple[1]

print('\nРазмер каталога (в Мб): {weight}'.format(weight=round(weight_file, 2)))
print('Количество подкаталогов: {count}'.format(count=count_dirs))
print('Количество файлов: {count}'.format(count=count_file))

