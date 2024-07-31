import random
class KillError(Exception):
	pass

class DrunkError(Exception):
	pass

class CarCrashError(Exception):
	pass

class GluttonyError(Exception):
	pass

class DepressionError(Exception):
	pass

class Karma:
	__day = 0
	__day_karma = 0
	__break_karma = 500
	__my_total_karma = 0
	__error_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

	def one_day(self):
			self.set_day()
			bad_day = random.randint(1,10)
			if bad_day == 1:
				error = self.__error_list[random.randint(0, 4)]
				try:
					raise error
				except error:
					self.print_error(error)
					with open('karma.log', 'a', encoding='utf-8') as file:
						file.write('В {day} день мы словили ошибку {error}\n'.format(day=self.get_day(), error=error))
			else:
				self.set_day_karma()
				self.set_my_total_karma()
				self.print_karma()


	def get_break_karma(self):
		return self.__break_karma

	def get_day(self):
		return self.__day

	def get_day_karma(self):
		return self.__day_karma

	def get_my_total_karma(self):
		return self.__my_total_karma

	def set_day(self):
		self.__day += 1

	def set_day_karma(self):
		self.__day_karma = random.randint(1,7)

	def set_my_total_karma(self):
		self.__my_total_karma += self.get_day_karma()

	def print_error(self, error):
		print('Сегодня {day} день и мы поймали исключение {error}'.format(day=self.get_day(), error=error))

	def print_karma(self):
		print('Сегодня {day} день, за день мы заработали {day_karma} кармы, у нас накопилось {karma} кармы'.format(
			day=self.get_day(),
			day_karma=self.get_day_karma(),
			karma=self.get_my_total_karma()
		))