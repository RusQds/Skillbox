class MyDict:
    def __init__(self):
        self.__my_dict = {1: 2, 2: 3, 3: 4}

    def set_my_dict(self, command, key=None, value=None):
        if command == 'append':
            self.__my_dict[key] = value
        elif command == 'pop':
            self.__my_dict.pop(key)

    def append(self, key, value):
        self.set_my_dict('append', key, value)

    def remove(self, key):
        return self.set_my_dict('pop', key)

    def get(self, key):
        return self.get_value(key)

    def get_value(self, key_search):
        for key, value in self.__my_dict.items():
            if key == key_search:
                return value
        return 0

my_dict = MyDict()
print(my_dict.get(4))