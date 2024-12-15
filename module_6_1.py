#Задача "Съедобное, несъедобное"

class Animal:
    """Класс Animal содержит наименование животного, жив он или мертв, сытый или голодный"""
    def __init__(self, name: str):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if not food.edible:
                print(f'{self.name} не стал есть {food.name}.')
                self.alive = False
            else:
                print(f'{self.name} съел {food.name}.')
                self.fed = True

class Plant:
    """Класс Plant содержит наименование растения, съедобное оно или нет"""
    def __init__(self, name: str):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name) # Волк с Уолл-Стрит
print(p1.name) # Цветик семицветик
print(a1.alive) # True
print(a2.fed) # False
a1.eat(p1) # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2) # Хатико съел Заводной апельсин
print(a1.alive) # False
print(a2.fed) # True
