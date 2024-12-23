#Задача "Записать и запомнить"

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    count_string = 0
    dict_ = {}
    for i in strings:
        num_cursor = file.tell()
        file.write(i +'\n')
        count_string += 1
        dict_.update({(count_string,num_cursor): i})
    return dict_

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')