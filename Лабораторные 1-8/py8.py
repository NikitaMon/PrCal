__author__ = "Монастыршин Никита"
"""
Задача 677в
Дана действительная матрица [aij]i, i = 1, ..., n. 
Получить действительную матрицу [bij]i, i = 1, ..., n элемент bij
которой равен сумме элементов данной 
матрицы расположенных в области, 
определяемой индексами i,j так, 
как показано на рисунке 36 (а - г) (область заштрихована). 
Сходным образом можно рассмотреть 
вместо суммы элементов их произведение, наибольшее значение, наименьшее значение.

https://ivtipm.github.io/Programming/Glava20/index20.htm#z677
"""

import numpy as np

mas = np.random.randint (0, 10, (10, 10))
print(mas)

print("Введите значения a")
i = int (input("Введите число i "))
j = int (input("Введите число j "))
i = i - 1


print("Матрица после обрезки")
mas2 = np.empty(((10-i)*j),dtype = int)

z = 0

for x in range (i,10):
    for y in range (0,j):
        mas2[z] = mas[x,y]
        z = z + 1

mas2.resize((10-i),j)

print(mas2)
print()


print("Получившаяся матрица")

qw = 10 - i - 1
#Вычисляет последнюю строку
for y in range (1,j):
    mas2[qw,y] = mas2[qw,y-1] + mas2[qw,y]

#Вычисляет нулевой столбец
for y in range (8-i,-1,-1):
    mas2[y,0] = mas2[y,0] + mas2[y+1,0]

#вычисляет оставшиеся значения
for x in range ((8-i),-1,-1):
    for y in range (1,j):
        mas2[x,y] = mas2[x+1,y] + mas2[x,y-1]

print(mas2)
print("Сумма", np.sum(mas2))
print("Минимум", mas2[9-i,0])
print("Максимум", mas2[0,j-1])
i2 = int (input("конец"))
