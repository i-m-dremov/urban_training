#1.Функция с параметрами по умолчанию:
#1.Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра
# со значениями по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'строка', c = True):
	# 2.Функция должна выводить эти параметры.
	print(a, b, c)
#3.Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(5)
print_params(5, 10)
print_params(5, 10, 15)
#4.Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c = [1,2,3])
print('*' * 40)
#2.Распаковка параметров:
#1.Создайте список values_list с тремя элементами разных типов.
values_list = [32, 'number', False]
#2.Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
values_dict = {'a': 69, 'b': 'Fish', 'c': True}
#3.Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
print('*' * 40)
#3.Распаковка + отдельные параметры:
#1.Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [True, 'apple']
#2.Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print('*' * 40)
