"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""
data = input('Введите строку символов: ')

def coding(data):
    code = ''
    sym1 = ''
    count = 1

    if not data:
        return ''

    for sym2 in data:
        if sym1 != sym2:
            if sym1:
                code += str(count) + sym1
            count = 1
            sym1 = sym2
        else:
            if count == 9:
                code += str(count) + sym1
                count = 1
            count +=1

    code += str(count) + sym1
    return code
code = coding(data)
print(code)

def decoding(data):
    decode = ''
    for i in range(0, len(data), 2):
        count, symbol = data[i: i + 2]
        decode += symbol * int(count)
    return decode
print(decoding(code))