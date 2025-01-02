#Домашнее задание по теме "Файлы в операционной системе"
import os
import time
from os.path import getmtime

# 1. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk('../..'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = getmtime(filepath)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
