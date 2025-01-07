#Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) for i in zip(first, second) if len(i[0]) != len(i[1]))
#second_result = (len([i]) == len([j]) for i in range(len(first)) for j in range(len(second)))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))   #[1, 2]
print(list(second_result))  #[False, False, True]
