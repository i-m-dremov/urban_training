#Задача "Вызов разом"

def apply_all_func(int_list, *function):
    result = {}
    for func in function:
        result.update({func.__name__: func(int_list)})
    return result

print(apply_all_func([6, 20, 15, 19.0], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))