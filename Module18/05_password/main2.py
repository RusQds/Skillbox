def int_sym(word):
    nums_list = [str(n) for n in range(10)]
    count = 0
    for sym in word:
        if sym in nums_list:
            count += 1

    if count >= 3:
        return True
    else:
        return False

def count_sym(word):
    if len(word) >= 8:
        return True
    else:
        return False

def upper_sym(word):
    nums_list = [str(n) for n in range(10)]
    for sym in password:
        if sym.upper() == sym and sym not in nums_list:
            return True
    return False

while True:
    password = input('Придумайте пароль: ')
    if upper_sym(password) and count_sym(password) and int_sym(password):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

