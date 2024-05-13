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
from Function8 import *

# обрезка матрицы
def lab8_matrix(mas, i, j):
    mas2 = np.empty(((10-i)*j),dtype = int)

    z = 0

    for x in range (i,10):
        for y in range (0,j):
            mas2[z] = mas[x,y]
            z = z + 1

    mas2.resize((10-i),j)

    return mas2

def lab8_result(mas, i, j):
    qw = 10 - i - 1
    #Вычисляет последнюю строку
    for y in range (1,j):
        mas[qw,y] = mas[qw,y-1] + mas[qw,y]

    #Вычисляет нулевой столбец
    for y in range (8-i,-1,-1):
        mas[y,0] = mas[y,0] + mas[y+1,0]

    #вычисляет оставшиеся значения
    for x in range ((8-i),-1,-1):
        for y in range (1,j):
            mas[x,y] = mas[x+1,y] + mas[x,y-1]

    return  mas, np.sum(mas), mas[9-i,0], mas[0,j-1]



if __name__ == "__main__":
    mas = np.random.randint (0, 10, (10, 10))
    print(mas)

    print("Введите значения a")
    i = int (input("Введите число i "))
    j = int (input("Введите число j "))
    i = i - 1

    print("Матрица после обрезки")
    mas = lab8_matrix(mas, i, j)
    print(mas)

    print("Получившаяся матрица")
    mas, sum, min, max = lab8_result(mas, i ,j)
    print(mas)
    print_sum_min_max(sum, min, max)