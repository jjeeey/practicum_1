"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 46.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дан одномерный массив числовых значений, насчитывающий N элементов. Дано положительное число T. Разделить это число между положительными элементами массива пропорционально значениям этих элементов и добавить полученные доли к соответствующим элементам.
#версия Python: 3.9.0
"""
import random
N = random.randint(1,25)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
T = random.randint(1,10)
print("T= " + str(T))
for i in range(N):
    if arr[i] > 0:
        t = arr[i]/T
        arr[i] = t
print(arr)
