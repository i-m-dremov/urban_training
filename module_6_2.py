class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        print(f'Модель {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя {self.__engine_power}')

    def get_color(self):
        print(f'Цвет {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() not in (x.lower() for x in self.__COLOR_VARIANTS):
            print(f'Нельзя сменить цвет на {new_color}')
        else:
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()   # Модель: Toyota Mark II
                        # Мощность двигателя: 500
                        # Цвет: blue
                        # Владелец: Fedos
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink') # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK') # Цвет должен поменяться
vehicle1.owner = 'Vasyok'   # Владелец должен поменяться
# Проверяем что поменялось.
vehicle1.print_info()  # Модель: Toyota Mark II
                        # Мощность двигателя: 500
                        # Мощность двигателя: 500
                        # Цвет: BLACK
                        # Владелец: Vasyok





