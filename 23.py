"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 23.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Даны вещественные числа X и Y . Вычислить Z. Z = √(X x Y) при X > Y, Z = ln(X + Y ) в противном случае.
#версия Python: 3.9.0
"""
import math
x = float(input("Введите вещественное число x:"))
y = float(input("Введите вещественное число y:"))
if x > y:
    z = math.sqrt(x * y)
    print(z)
else:
    z = math.log(x + y, math.e)
    print(z)
