"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 12.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дано вещественное число. Определите, какое это число:положительное, отрицательное,ноль.
#версия Python: 3.9.0
"""
num = float (input("Введите вещественное число:"))
if (num == 0):
    print("Число - 0")
elif (num > 0):
    print("Число положительное")
else:
    print("Число отрицательное")