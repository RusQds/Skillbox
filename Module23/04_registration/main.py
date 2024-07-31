def save_registrations_good(string):
	with open('registrations_good.log', 'a', encoding='utf-8') as file:
		file.write('{}\n'.format(string))

def save_registrations_bad(string, error):
	with open('registrations_bad.log', 'a', encoding='utf-8') as file:
		file.write('{0} - Ошибка {1}\n'.format(string, error))

def valid_account(account):
	if len(account) < 3:
		raise IndexError
	elif not account[0].isalpha():
		raise NameError
	elif '@' not in account[1] or '.' not in account[1]:
		raise SyntaxError
	elif int(account[2]) not in range(10, 99):
		raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as file:
	for i_line in file:
		account = i_line[:i_line.index('\n')]
		account_list = account.split(' ')
		try:
			valid_account(account_list)
			save_registrations_good(account)
		except IndexError:
			save_registrations_bad(account, 'IndexError - НЕ присутствуют все три поля')
		except NameError:
			save_registrations_bad(account, 'NameError - поле имени содержит НЕ только буквы')
		except SyntaxError:
			save_registrations_bad(account, 'SyntaxError - Поле емейл НЕ содержит @ и .(точку)')
		except ValueError:
			save_registrations_bad(account, 'ValueError - Поле возраст НЕ является числом от 10 до 99')

# Принято



