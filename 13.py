"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 13.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Можно ли из бревна, имеющего диаметр поперечного сечения D, выпилить квадратный брус шириной А?
#версия Python: 3.9.0
"""
import math
D = int(input("Введите диаметр поперечного сечения:"))
A = int(input("Введите ширину квадратного бруса:"))
A = math.sqrt(2) * A
print("Диагональ бруса равна",A)
if (A <=D):
    print("Выпилить квадратный брус шириной ",A,"возможно")
else:
    print("Выпилить квадратный брус шириной ", A, "невозможно")
