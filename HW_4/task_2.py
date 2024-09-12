"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

import random

number = int(input('Введите размер списка: '))

new_list = [random.randint(0, number) for i in range(number)]
uni = [i for i in new_list if new_list.count(i) == 1]
print(new_list)
print(uni)
