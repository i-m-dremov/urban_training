# Задание: Декораторы в Python

# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number <= 1:
            print('Не относится ни к простым числам ни к составным')
        for i in range(2, int(number ** 0.5) + 1):
            if number % i != 0:
                return f'Простое\n{number}'
        return f'Составное\n{number}'
    return wrapper

@is_prime
def sum_three(*args):
    results = sum(args)
    return results

result = sum_three(2, 3, 6)
print(result)

# Результат консоли:
# Простое
# 11
