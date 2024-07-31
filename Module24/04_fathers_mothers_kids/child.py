class Child:

	def __init__(self, name, age, calm_state='бешеный', state_of_hunger='голодный'):
		self.name=name
		self.age=age
		self.calm_state=calm_state
		self.state_of_hunger=state_of_hunger

	def info(self):
		print('\n\tИмя: {name}\n\tВозраст: {age}\n\tСостояние спокойствия: {calm_state}\n\tСостояние голода: {state_of_hunger}'.format(
			name=self.name,
			age=self.age,
			calm_state = self.calm_state,
			state_of_hunger = self.state_of_hunger
		))