import os

# C:\Python310\python.exe "C:/Users/maxim/OneDrive/Рабочий стол/skillbox/Python_Basic/Module22/05_save/elements.py"
# Введите строку: asd
# Куда хотите сохранить документ? Введите последовательность папок (через пробел):
# C:\
# Введите имя файла: text.txt
# C:\text.txt
# Traceback (most recent call last):
#   File "C:\Users\maxim\OneDrive\Рабочий стол\skillbox\Python_Basic\Module22\05_save\elements.py", line 34, in <module>
#     search_path(path, text)
#   File "C:\Users\maxim\OneDrive\Рабочий стол\skillbox\Python_Basic\Module22\05_save\elements.py", line 16, in search_path
#     save_file(path_file, text)
#   File "C:\Users\maxim\OneDrive\Рабочий стол\skillbox\Python_Basic\Module22\05_save\elements.py", line 5, in save_file
#     open_file = open(path, 'w')
# PermissionError: [Errno 13] Permission denied: 'C:\\text.txt'
#
# Process finished with exit code 1

# Ошибка которую я получаю при попытке сохранить файл.
# Попробовал программу с диском D, файл успешно был создан. Видимо на диск C файл пытается сохраниться без прав
# администратора, хотя я работаю с отсновной учетной записи.

def save_file(path, text):
	print('Пытаюсь открыть', path)
	open_file = open(path, 'w')
	open_file.write(text)
	print('Файл успешно сохранён!')
	open_file.close()


def search_path(path, text):
	if os.path.exists(path):
		file_name = input('Введите имя файла: ')
		path_file = os.path.join(path, file_name)
		print(path_file)
		if file_name not in os.listdir(path):
			save_file(path_file, text)
		else:
			q = input('Вы действительно хотите перезаписать файл? (да, нет): ')
			if q.lower() == 'да':
				save_file(path_file, text)
	else:
		print('Такой путь не найден!')


text = input('Введите строку: ')
path_list = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(
	' ')
path = os.path.join('D:', os.path.sep)
for i_elem in path_list:
	path = os.path.join(path, i_elem)
print(path)

# path = 'Users maxim OneDrive Рабочий^ стол skillbox Python_Basic Module22 05_save'
search_path(path, text)

# Принято
