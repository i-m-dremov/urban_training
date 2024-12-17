#Задача "Ошибка эволюции"

from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 5

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        step_dx = self._cords[0] + dx * self.speed
        step_dy = self._cords[1] + dy * self.speed
        step_dz = self._cords[2] + dz * self.speed
        if step_dz < 0:
            print("It's too deep, i cn.t dive :(")
        else:
            self._cords = [step_dx, step_dy, step_dz]

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I`m peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    def __init__(self, _DEGREE_OF_DANGER):
        super().__init__(_DEGREE_OF_DANGER)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = int(self._cords[2] - (abs(dz) * self.speed / 2))

class PoisonAnimal(Animal):
    def __init__(self, _DEGREE_OF_DANGER):
        super().__init__(_DEGREE_OF_DANGER)
        self._DEGREE_OF_DANGER = 8

class Duckbill(PoisonAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'
    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)
print(db.live)                  # True
print(db.beak)                  # True
db.speak()                      # Click-click-click
db.attack()                     # Be careful, I'm attacking you 0_0
db.move(1, 2, 3)
db.get_cords()                  # X: 10 Y: 20 Z: 30
db.dive_in(6)
db.get_cords()                  #X: 10 Y: 20 Z: 0
db.lay_eggs()                   # Here are(is) 3 eggs for you # Число может быть другим (1-4)
