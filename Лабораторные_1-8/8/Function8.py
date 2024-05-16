__author__ = "Монастыршин Никита"
import numpy as np

# обрезка матрицы
def lab8_matrix(mas, i, j):
    """Обрезает матрицу по i и j как в задании"""
    mas2 = np.empty(((10-i)*j),dtype = int) # создание массива 
    z = 0
    # заполнение обрезанного массива
    for x in range (i,10):
        for y in range (0,j):
            mas2[z] = mas[x,y]
            z = z + 1

    mas2.resize((10-i),j)

    return mas2

# вычисление параметров обрезанной матрицы
def lab8_result(mas):
    """Вычисляет сумму, минимальное и максимальное значение"""
    i = 10 - len(mas)
    j = len(mas[0])

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