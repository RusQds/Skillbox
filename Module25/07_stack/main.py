
class Steck:
	def __init__(self):
		self.__objects_list = list()

	def add(self, task):
		if task not in self.__objects_list:
			self.__objects_list.append(task)
			print('Добавляем задачу {task} в менеджер'.format(task=task))
		else:
			print('Задача {task} уже есть в менеджере!'.format(task=task))


	def delete(self):
		if len(self.__objects_list) != 0:
			task = self.__objects_list.pop(-1)
			print('\nЗадача {task} удалена из менеджера'.format(task=task))
		else:
			print('\nЗадач в менеджере не найдено!')

	def get_last(self):
		if len(self.__objects_list) != 0:
			return self.__objects_list[-1]
		else:
			return False

	def get_all(self):
		return self.__objects_list

class TaskManager:

	def __init__(self):
		self.steck_dict = dict()

	def __str__(self):
		return ''.join(['\nЗадача {priority} приоритета: {task}'.format(priority=i_elem, task=j_elem) for i_elem in
										sorted(self.steck_dict) for j_elem in self.steck_dict[i_elem].get_all()])

	def new_task(self, task, priority):
		if priority not in self.steck_dict:
			self.steck_dict[priority] = Steck()
			self.steck_dict[priority].add(task)
		else:
			self.steck_dict[priority].add(task)

#Не понял как именно реализовать удаление, по приоритету или по задаче или из всх приоритетов сразу.
#Реализовал просто удаление последней задачи из последнего приоритета.
	def del_task(self):
		if len(self.steck_dict) > 0:
			self.steck_dict[max(self.steck_dict.keys())].delete()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task()
print(manager)
manager.del_task()
print(manager)

# Принято
