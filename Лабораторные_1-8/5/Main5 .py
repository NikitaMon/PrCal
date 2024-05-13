__author__ = "Монастыршин Никита"
"""
Задание 136И
Даны натуральное число n, действительные числа a1,..., an. Вычислить:

https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
"""

import random
import numpy as np
from Function5 import *

def lab5(n,mas):
    res = 0     #сумма
    fact = 1    #значение факториала
    hf = 1      #следующая переменная на которую домнажается

    # a = random.randint(0,10)
    # факториал 0! = 1
    #           1! = 1
    # a / (n-1)!
    for i in range(0,n):
        buf = mas[i] / fact  #заполнение массива
        fact = fact * hf    #следующее значение факториала
        hf = hf + 1         #следующая переменная для домножения
        res = res + buf  #вычисление результата
    return res


if __name__ == "__main__":
    print("Лабораторная №5")
    n = int (input("Введите число n "))
    mas = np.random.randint (0, 10, n) # создание массива с числами от 0 до 9 в количестве n
    print_res(lab5(n,mas))
