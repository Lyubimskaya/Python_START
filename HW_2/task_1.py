"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
number = input()
sum_number = 0
for lm in number:
    if lm.isdigit():
        sum_number += int(lm)
print(f"Сумма цифр равна: {sum_number}")