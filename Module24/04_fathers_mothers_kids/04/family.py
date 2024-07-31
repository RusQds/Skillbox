class Children:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = True
        self.hangry = False

    def get_name(self):
        return self.name

    def get_info(self):
        print("\nMy name: {}\nMy age: {}\nCalm status: {}\nHangry statue: {}".format(self.name, self.age, self.calm, self.hangry))

    def set_calm_down(self):
        self.calm = True
        print('\n###{}###\nЯ спокоен!'.format(self.name))

    def set_calm_up(self):
        self.calm = False
        print('\n###{}###\nЯ разозлился!'.format(self.name))

    def set_hangry_down(self):
        self.hangry = False
        print('\n###{}###\nЯ наелся!'.format(self.name))

    def set_hangry_up(self):
        self.hangry = True
        print('\n###{}###\nЯ голодный!'.format(self.name))
class Parent:

    def __init__(self, name, age, children_list=[]):
        self.name = name
        self.age = age
        self.children_list = children_list

    def get_info(self):
        print("\nMy name: {}\nMy age: {}\nMy childrens: {}".format(self.name, self.age, ', '.join([children.get_name() for children in self.children_list])))

    def children_calm_down(self, children):
        print('\n###{}###\nУспокаиваю ребенка {}'.format(self.name, children.get_name()))
        children.set_calm_down()

    def children_hangry_down(self, children):
        print('\n###{}###\nКормлю ребенка {}'.format(self.name, children.get_name()))
        children.set_hangry_down()