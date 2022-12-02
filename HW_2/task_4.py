"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""
import random
num = int(input("Введите число: "))
new_list = [random.randint(-num, num) for r in range(num)]
index_list = []
res = 1
with open('indexes.txt', encoding = 'UTF-8') as data:
    for index in data:
        index_list.append(int(index))
for i in range(-num, num):
    if i in index_list:
        res *= new_list[i]
print(res)
