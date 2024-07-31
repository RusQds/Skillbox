class Stack:
    __index = 0

    def __init__(self):
        self.__index = Stack.__index
        self.__next = None
        self.__value = None
        self.set_index()

    def __str__(self):
        return 'Индекс {index} - значение {value}'.format(index=self.get_index(),
                                                          value=self.get_value())

    def get_index(self):
        return self.__index

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    @staticmethod
    def set_index():
        Stack.__index += 1

    def set_value(self, value):
        self.__value = value

    def append(self, value):
        previous_node = self
        next_node = previous_node.get_next()
        while isinstance(next_node, Stack):
            previous_node = next_node
            next_node = previous_node.get_next()
        if not isinstance(next_node, Stack):
            previous_node.set_value(value)
            previous_node.set_next(Stack())

    def remove(self):
        previous_node = self
        next_node = previous_node.get_next()
        while isinstance(next_node.get_next(), Stack):
            previous_node = next_node
            next_node = previous_node.get_next()
        if isinstance(previous_node.get_next(), Stack):
            previous_node.set_next(None)


my_stack = Stack()

print('\nДобавляем')
my_stack.append(10)
my_stack.append(20)
my_stack.append(50)

my_node = my_stack

while isinstance(my_node.get_next(), Stack):
    print(my_node)
    my_node = my_node.get_next()

print('\nУдаляем')
my_stack.remove()

my_node = my_stack
while isinstance(my_node.get_next(), Stack):
    print(my_node)
    my_node = my_node.get_next()
