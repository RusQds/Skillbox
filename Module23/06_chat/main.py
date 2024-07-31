import time

def look_chat_log():
	with open('chat_log.log', 'r', encoding='utf-8') as chat_log:
		for i_line in chat_log:
			print(i_line)
		print('\n')

def write_chat(name):
	with open('chat_log.log', 'a', encoding='utf-8') as chat_log:
		text = input('Введите сообщение: ')
		chat_log.write('{0} - {1}: {2}\n'.format(time.ctime(), name, text))


name = input('Введите имя пользователя: ')
print('Добрый день {0}!'.format(name))
while True:
	print('\nКакое действие желаете выполнить?')
	command = int(input('1. Посмотреть текущий текст чата\n2. Отправить сообщение \n'))
	if command == 1:
		try:
			look_chat_log()
		except FileNotFoundError:
			print('В чат пока никто не писал')
	elif command == 2:
		write_chat(name)
	else:
		print('Комманда не распознана, попробуйте снова.')

# Принято

