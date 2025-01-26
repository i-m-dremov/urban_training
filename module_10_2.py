# Задача "За честь и отвагу!":

import time
import threading
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:

class Knight(threading.Thread):
    enemy_power = 100
    day = 0
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        while self.enemy_power > 0:
            self.day += 1
            self.enemy_power -= self.power
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemy_power} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
