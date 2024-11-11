#Задание "Слишком древний шифр"
import random

x = 0 #Числ,о которое выпадает рандомно
stone = [] # список чисел из которых выбирается число на первом камне
cod = [] #переменная в которую записываются все пары
def stone_riddle():  #Функция создания рандомного числа в первом поле
	for i in range(3, 20 + 1): #Значение на первом камне от 3 до 20(включительно)
		stone.append(i)
		x = random.choice(stone)
	print(f'Число на первом камне: {x}')
	return x
result = stone_riddle()
for i in range(1, result):
	for j in range(len(stone), i, -1):
		if i == j:
			break
		if result % (i + j) == 0:
			cod += i, j
			break
print('Result: ', end='')
print(*cod, sep='')

