"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 17.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R. Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.
#версия Python: 3.9.0
"""
import math
A = int(input("Ребро кубической ёмкости:"))
H = int(input("Высота цилиндрической ёмкости:"))
R = int(input("Радиус основания цилиндрической ёмкости:"))
M = int(input("Введите объем жидкости:"))
CK = A ** 3
print(CK, "Объём куба")
KC = math.pi * R ** 2 * H
print(KC, "Объём цилиндра")
if M < KC and M < CK:
    print("Жидкость поместится в оба сосуда")
if M < KC:
    print("Жидкость поместится в цилиндр")
if M < CK:
    print("Жидкость поместится в куб")
