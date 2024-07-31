def ip_controll(ip):
	for i in ip:
		if not i.isdigit():
			print(i, '- не целое число')
			return
		if int(i) > 255:
			print(int(i), 'превышает 255')
			return
	print('IP-адрес корректен')


while True:
	ip_address = input('Введите IP: ').split('.')
	if len(ip_address) < 4:
		print('Адрес - это четыре числа, разделенные точками')
	else:
		ip_controll(ip_address)


# Принято
