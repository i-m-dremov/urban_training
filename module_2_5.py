#Задача "Матрица воплоти":
#Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
n = 0 #количество строк
m = 0 #количество столбцов
value = 0 #значения данных в матрице
def get_matrix(n, m, value):
	matrix = []
	if n <= 0:
		return matrix
	elif m <= 0:
		return matrix
	for i in range(n):
		matrix.append([])
		for j in range(m):
			matrix[i].append(value)
	return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
