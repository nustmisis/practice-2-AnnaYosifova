# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми
шли три цифры. После того как все возможные номера были использованы, формат был изменен на четыре цифры, предшествующие
трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак машины и оповещающую о том, для какого формата подходит
данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному
из двух форматов, укажите это в сообщении.
"""


def check_plate_format(license_plate):
    if len(license_plate) == 6 and license_plate[-3:].isdigit() and license_plate[:3].isupper():
        print('Номер соответствует старому формату.')
    elif len(license_plate) == 7 and license_plate[:4].isdigit() and license_plate[-3:].isupper():
        print('Номер соответствует новому формату.')
    else:
        print('Номер не соответствует ни старому, ни новому формату, проверьте его правильность.')


while True:
    license_plate = input("Введите номерной знак машины: ")
    check_plate_format(license_plate)


# Вариант с регулярками для номеров в русскими буквами
# import re
#
#
# def check_plate_format(license_plate):
#     old_format_pattern = r'^[А-Я]{3}\d{3}$'
#     new_format_pattern = r'^\d{4}[А-Я]{3}$'
#
#     if re.match(old_format_pattern, license_plate):
#         return "Номер соответствует старому формату."
#     elif re.match(new_format_pattern, license_plate):
#         return "Номер соответствует новому формату."
#     else:
#         return "Номер не соответствует ни старому, ни новому формату."
#
#
# while True:
#     license_plate = input("Введите номерной знак машины: ")
#
#     result = check_plate_format(license_plate)
#     print(result)
