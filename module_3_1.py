calls = 0
# Функция подсчета вызовов других функций.
def count_calls():
	global calls
	calls += 1
# Функция принимает аргумент - строку и возвращает кортеж из: длины этой строки,
# строку в верхнем регистре, строку в нижнем регистре.
def string_info(string): #
	count_calls()
	string = (len(string), string.upper(), string.lower())
	return string
# Функция принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебрегаем
def is_contains(string, list_to_search):
	count_calls()
	if string.lower() in [s.lower() for s in list_to_search]:
		return True
	else:
		return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)