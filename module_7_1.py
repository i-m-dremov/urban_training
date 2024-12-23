#Задача "Учёт товаров"

class Shop():

    def __init__(self,file_name = 'products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file_read = open(self.__file_name, 'r')
        file_list = file_read.read()
        file_read.close()
        return file_list

    def add(self, *products):
        file_append = open(self.__file_name, 'a')
        for i in products:
            if str(i) in self.get_products():
                print(f'Продукт {str(i)} уже есть в магазине')
            else:
                file_append.write(str(i) + '\n')
        file_append.close()

class Product(Shop):
    def __init__(self, name: str, weight: float, category: str):
        self.name = name                    #название продукта
        self.weight = weight                #общий вес товара (5.4, 52.8 и т.п.).
        self.category = category            #категория товара (строка).

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

# Пример работы программы:

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

# Вывод на консоль:

# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables