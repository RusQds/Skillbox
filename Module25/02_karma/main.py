from karma import Karma

my_karma = Karma()
while True:
	my_karma.one_day()
	if my_karma.get_my_total_karma() >= my_karma.get_break_karma():
		break

# Принято
