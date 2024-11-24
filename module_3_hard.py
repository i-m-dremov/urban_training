#Задание "Раз, два, три, четыре, пять .... Это не всё?":
#Необходимо просуммировать все значения в списке, если значение не число то суммируется длина строки
#Исходные данные
data_structure = [
	[1, 2, 3],  # -list 6
	{'a': 4, 'b': 5},  # - dict 11
	(6, {'cube': 7, 'drum': 8}),  # - tuple 29
	'Hello',  # - str 5
	((), [{(2, 'Urban', ('Urban2', 35))}])  # - tuple 48
]


def calculate_structure_sum(data):
	summ = 0
	if isinstance(data, (list, set, tuple)):  		# Проверяем к какому типу относится элемент 1 (2,3...) уровня
		for item in data:  							# Проходим по каждому элементу 2(3,4...) уровня
			summ += calculate_structure_sum(item)  	# В переменную summ прибавляем результат от действия функции на
													# элемент 2(3,4...) уровня

	elif isinstance(data, dict):  					# Проверяем на тип dict отдельно, потому-что внутри 2 элемента
		for key, value in data.items():
			summ += calculate_structure_sum(key)  	# Отдельно применяем функцию к ключу и значению словаря
			summ += calculate_structure_sum(value)
													# Основа суммирования, этот участок также отвечает
													# за проверку значений item, число сразу суммируется,
													# строка (прибавляется длина)
	elif isinstance(data, (int, float)):
		summ += data
	elif isinstance(data, str):
		summ += len(data)

	return summ


result = calculate_structure_sum(data_structure)
print(result)