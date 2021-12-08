"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re
from chardet import detect


def get_data():
    files = ["info_1.txt", "info_2.txt", "info_3.txt"]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in files:
        # перезапись файла в нужной кодировке
        with open(file, 'rb') as f:
            content_bytes = f.read()
        detected = detect(content_bytes)
        encoding = detected['encoding']
        content_text = content_bytes.decode(encoding)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content_text)
        # открываем файл в правильной кодировке
        with open(file, 'r', encoding='utf-8') as f_n:
            data = f_n.read()
            # Получаем список изготовителей системы
            os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
            os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
            # Название ОС
            os_name_reg = re.compile(r'Windows\s\S*')
            os_name_list.append(os_name_reg.findall(data)[0])
            # Код продукта
            os_code_reg = re.compile(r'Код продукта:\s*\S*')
            os_code_list.append(os_code_reg.findall(data)[0].split()[2])
            # Тип системы
            os_type_reg = re.compile(r'Тип системы:\s*\S*')
            os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    for line in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
        main_data.append(list(line))

    return main_data


def write_to_csv(file):
    main_data = get_data()
    with open(file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('report.csv')
