"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 50.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дан одномерный массив числовых значений, насчитывающий N элементов. Подсчитать количество чисел, делящихся на 3 нацело, и среднее арифметическое чисел с чётными значениями. Поставить полученные величины на первое и последнее места в массиве (увеличив массив на 2 элемента).
#версия Python: 3.9.0
"""
import random
N = random.randint(1,15)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
K = 0
T = 0
t = 0
for i in range(N):
    if arr[i] % 3 ==0:
        K += 1
print("Кол-во чисел кратных трём: " +str(K))

for i in range(N):
    if arr[i] % 2==0:
        T += arr[i]
        t += 1
A = T/t
print("Арифметическое значение: " + str(A))
arr.insert(0, K)
arr.append(A)
print(arr)
