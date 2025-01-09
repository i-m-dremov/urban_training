print('Задача "Функциональное разнообразие"')
print('*' * 120)
print('Lambda функция')
#Lambda-функция:
#Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
#Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
#Здесь ? - место написания lambda-функции.
print(list(map(lambda x,y: x == y, first, second)))
print('*' * 120)
#Результатом должен быть список совпадения букв в той же позиции:
#[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#Где True - совпало, False - не совпало.
print('Замыкание')
# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.
# Данный код:
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Запишет данные в файл в таком виде:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, mode='w', encoding='UTF-8') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print('Проверь файл')
print('*' * 120)

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words
# и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете
# использовать функцию choice из модуля random.
# Ваш код (количество слов для случайного выбора может быть другое):

from random import choice
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        word = choice(self.words)
        return word
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print('*' * 120)