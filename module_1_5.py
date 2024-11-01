#2
immutable_var = 456, 25.4, 'word', False
print(immutable_var)
#3

#immutable_var[1] = 30
# #Изменить элемент кортежа не возможно, потому что кортеж не хранит список, он хранит ссылку на список

#При очень большом желании можно преобразовать кортеж в список, заменить элемент и вернуть список в кортеж,
#но это не замена элемента в кортеже))
immutable_var = 456, 25.4, 'word', False
lst = list(immutable_var)
lst[1] = 30
immutable_var = tuple(lst)
print(immutable_var)

#4
mutable_list = [456, 25.4, 'word', False]
mutable_list[1] = 30
mutable_list[3] = True
print(mutable_list)