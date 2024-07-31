import time
import os

def new_message(name):
    os.system('cls' if os.name == 'nt' else 'clear')
    message = input('Введите сообщение: ')
    now_time = time.ctime()
    with open('chat.log', 'a', encoding='utf-8') as chat_text:
        chat_text.write(f'{now_time} - {name} : {message}\n')

def read_messages():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('chat.log', 'r', encoding='utf-8') as chat_text:
        for message in chat_text.read().split('\n'):
            print(f'{message}\n')
            time.sleep(1)

while True:
    name = input('Введите имя пользователя: ')
    print('\nКакое действие желаете выполнить?')
    command = int(input('1. Посмотреть текущий текст чата\n2. Отправить сообщение \n'))
    if command == 1:
        read_messages()
    elif command == 2:
        new_message(name)
    else:
        print('Комманда не распознана!')