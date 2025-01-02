# Задание "Они все так похожи"
# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
# объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированы и для них должны
# быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: object = True):
        self.__color = list(color)
        self.filled = filled
        self.__sides = sides

    '''Служебный метод get_color возвращает список RGB цветов.'''
    def get_color(self):
        return self.__color

    '''Метод get_sides должен возвращать значение я атрибута __sides.'''
    def get_sides(self):
        return self.__sides
    '''служебный метод __is_valid_color, принимает параметры r, g, b, который проверяет корректность
    переданных значений перед установкой нового цвета.Корректным цвет: все значения r, g и b - целые числа
    в диапазоне от 0 до 255 (включительно).'''

    def is_valid_color(self, *color: int):
        self.list_new_color = list(color)
        if min(*self.list_new_color) < 0  or max(*self.list_new_color) > 250:
            return False
        else:
            return True

    '''Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color
    на соответствующие значения, предварительно проверив их на корректность. 
    Если введены некорректные данные, то цвет остаётся прежним.'''
    def set_color(self, *color: int):
        if self.is_valid_color(*color):
            self.__color = [*color]

    '''Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True
    если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
    False - во всех остальных случаях.'''
    def __is_valid_sides(self, *sides):
        new_sides_count = list(sides)
        if min(new_sides_count) > 0 and len(new_sides_count) == self.sides_count:
            return True
        else:
            return False

    '''Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
     то не изменять, в противном случае - менять.'''
    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [i for i in sides]
        else:
            self.__sides = [self.__sides[0]] * self.sides_count

    '''Метод __len__ должен возвращать периметр фигуры.'''
    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__() / (2 * pi) #self.__len__() / (2 * pi)

    def get_square(self):
        return (self.__radius() ** 2) * pi

class Triangle(Figure):
    sides_count = 3
    h_m = 0

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled = True)

    def get_square(self):
        h_m = self.__len__() / 2
        return sqrt(h_m * (h_m - super().get_sides()[0])*(h_m - super().get_sides()[1])*(h_m - super().get_sides()[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled = True)

    def get_volume(self):
       return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10, 12) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6) # (Цвет, стороны)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())                              # [55, 66, 77]
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())                                # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())                                # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15) # Изменится
print(circle1.get_sides())                              # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))                                     # 15

# Проверка объёма (куба):
print(cube1.get_volume())                               # 216

#дополнительная проверка
print(circle1.get_square())   # 17.90

triangle1 = Triangle((150, 66, 13), 5)
print(triangle1.get_color())
triangle1.set_color(150, 150, 150)
print(triangle1.get_color())
triangle1.set_sides(10, 15, 20)
print(triangle1.get_sides())
print(len(triangle1))
print(triangle1.get_square())
