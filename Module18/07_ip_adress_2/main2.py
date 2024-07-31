def elem_control(ip_adress:str):
    ip_adress_list = ip_adress.split('.')
    if ip_adress.count('.') != 3 or len(ip_adress_list) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return False
    else:
        for elem in ip_adress_list:
            if not elem.isdigit():
                print('{} - не целое число'.format(elem))
                return False
            if elem.isdigit() and int(elem) > 255:
                print('{} превышает 255'.format(elem))
                return False
        return True

while True:
    ip_adress = input('Введите IP: ')
    if elem_control(ip_adress):
        print('IP-адрес корректен')
        break