#Задача "Developer - не только разработчик":

class House:

	def __init__(self, name, number_of_floors):
		self.name = name
		self.number_of_floors = number_of_floors

	def goto(self, new_floor):
		if new_floor > self.number_of_floors:
			print(f'Такого этажа в {self.name} не существует')
		else:
			for i in range(new_floor):
				print(f' Этаж {i + 1} в {self.name}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.goto(5)
h2.goto(10)
