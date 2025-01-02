#Домашнее задание по уроку "Try и Except".

def add_everything_up(a, b):
    try:
        c = a + b
    except TypeError as exc:
        return f'Ошибка {exc.args}, поэтому получилось, {str(a) + str(b)}'
    else:
        return f"Получилось что-то типа, {round(c, 3)}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
