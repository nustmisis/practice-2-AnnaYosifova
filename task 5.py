# -*- coding: utf-8 -*-
"""
Задана строка S и символ С. За один ход можно поменять местами два соседних символа. Сколько потребуется ходов чтобы
переместить все символы С в строке в начало строки, не меняя при этом порядок следования между остальным символами.

Например, имеется строка abcabcabc, и задан символ b. После перемещения всех символов b в начало строки, получится строка 
bbbacacac, на это уйдёт 9 ходов, ниже указаны строки получившиеся после кажого хода.
1. bacabcabc

2. bacbacabc

3. babcacabc

4. bbacacabc

5. bbacacbac

6. bbacabcac 

7. bbacbacac

8. bbabcacac 

9. bbbacacac
Входные данные

Задана строка 5, состоящая из прописных бука латинского алфавита, и символ С через пробел.
Длина строки не превышает 100 символов. Гарантируется, что символ С встречается в строке 5.

Выходные данные

Выведите единственное числе количество ходов, которое потребуется, чтобы переместить все символы с начало строки

Примеры

входные данные

аbrahcabe b

выходные данные
7

@author: workk
"""


def count_moves_to_start(str):
    s, c = str.split()
    str_list = list(s)
    count = 0
    i = 0

    while i < len(str_list):
        if str_list[i] == c and i == 0:
            i += 1
            continue

        if str_list[i] == c:
            j = i
            while j > 0 and str_list[j - 1] != c:
                str_list[j], str_list[j - 1] = str_list[j - 1], str_list[j]
                count += 1
                j -= 1
        i += 1

    return count


while True:
    try:
        str = input("Введите строку и символ (например abahfbfb b): ")
        print(count_moves_to_start(str))
    except Exception as e:
        print("Проверьте корректность данных и введите их снова.")
        continue
