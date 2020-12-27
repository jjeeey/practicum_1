"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 30.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/12/2020
Дата последней модификации: 11/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задачи № 1-101 практикума № 1
Составьте блок-схему поиска максимального элемента в одномерном массиве.
#версия Python: 3.9.0
"""
import random
N = 10
A = [random.randint(0, 100) for i in range(N)]
print(A)
print("Max =", max(A))