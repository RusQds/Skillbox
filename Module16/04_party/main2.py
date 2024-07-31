def command_guests(guests, command):
    if command == 'пришел':
        name_guest = input('Имя гостя: ')
        add_guests(guests, name_guest)
    if command == 'ушел':
        name_guest = input('Имя гостя: ')
        remove_guests(guests, name_guest)
    if command == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        return False
    return True

def remove_guests(guests, name):
    guests.remove(name)
    print(f'Пока, {name}!')

def add_guests(guests, name):
    if len(guests) >= 6:
        print(f'Прости, {name}, но мест нет.')
    else:
        guests.append(name)
        print(f'Привет, {name}!')

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    command = input('Гость пришел или ушел? ')
    flag = command_guests(guests, command)
    if flag is False:
        break