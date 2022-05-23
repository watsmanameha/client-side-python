"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений или другого инструмента извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    files_names_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    keys = [('Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы')]

    for el in keys:
        main_data.append(el)

    for f_n in files_names_list:
        file = open(f_n, encoding='utf-8')
        data = file.read()

        os_prod_match = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_match.findall(data)[0].split()[2])

        os_name_match = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_match.findall(data)[0])

        os_code_match = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_match.findall(data)[0].split()[2])

        os_type_match = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_match.findall(data)[0].split()[2])

    j = 1
    for i in range(0, 3):
        row_data = []
        row_data.append(j)
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)
        j += 1
    return main_data

    # print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)


def write_to_csv(f_n):
    main_data = get_data()
    with open(f_n, 'w', encoding='utf-8') as f:
        writer =csv.writer(f)
        for row in main_data:
            writer.writerow(row)

write_to_csv('data_report_1.csv')