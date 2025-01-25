# Задача "Потоковая запись в файлы":
import time
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='UTF-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_1 = time.time()
print(f'Работа потоков 0: {time_end_1 - time_start_1}')

time_start_2 = time.time()
thread_1 = Thread(target=write_words, args = (10, 'example5.txt'))
thread_2 = Thread(target=write_words, args = (30, 'example6.txt'))
thread_3 = Thread(target=write_words, args = (200, 'example7.txt'))
thread_4 = Thread(target=write_words, args = (100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

time_end_2 = time.time()
print(f'Работа потоков 0: {time_end_2 - time_start_2}')