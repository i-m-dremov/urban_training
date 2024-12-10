#Задача "История строительства":

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args [0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def goto(self, new_floor):
        if new_floor > self.number_of_floors:
            print(f'Такого этажа в {self.name} не существует')
        else:
            for i in range(new_floor):
                print(f' Этаж {i + 1} в {self.name}')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            return print('Объекты не соответствуют типу House')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            return print('Новый операнд должен быть типом int')
        else:
            self.number_of_floors += value
            return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history) # ['ЖК Эльбрус']
h2 = House('ЖК Акация', 20)
print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация']
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# # Удаление объектов
del h2 # ЖК Акация снесён, но он останется в истории
del h3 # ЖК Матрёшки снесён, но он останется в истории
print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
                            # ЖК Эльбрус снесён, но он останется в истории
