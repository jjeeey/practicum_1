"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 51.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Заданы M строк символов, которые вводятся с клавиатуры. Найти количество символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив перед каждой строкой соответствующее количество звёздочек.
#версия Python: 3.9.0
"""
M = int(input("Введите количество строк: "))
x = []
for i in range(0, M):
    print("Введите строку:",  end=' ')
    x.append(input())
maxx= 0
for y in x:
    d = len(y)
    if d > maxx:
        maxx = d
print("Максимальная длина строки:", maxx)
for y in x:
    d = len(y)
    if d < maxx:
        for i in range(0, maxx - d):
            y = '*' + y
    print(y)