from family import *

children_1 = Children('Саша', 5)
children_2 = Children('Дима', 7)


Mother = Parent('Николь', 32, [children_1, children_2])

Mother.get_info()
children_1.get_info()
children_2.get_info()
children_1.set_hangry_up()
children_2.set_calm_up()
children_1.get_info()
children_2.get_info()

Mother.children_hangry_down(children_1)
Mother.children_calm_down(children_2)
children_1.get_info()
children_2.get_info()