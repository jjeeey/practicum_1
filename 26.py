"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 26.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дано вещественное число A. Вычислить f(A), если f(x) = 0, при x ≤ 0; f(x) = x при 0 < x < 1, в противном случае f(x) = x4.
#версия Python: 3.9.0
"""
import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(A) =:", fx)
elif 0 < x < 1:
    fx = x
    print("0 < x < 1; f(A) =:", fx)
else:
    fx = math.pow(x, 4)
    print("x >= 1; f(A) =:", fx)
