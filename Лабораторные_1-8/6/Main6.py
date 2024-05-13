__author__ = "Монастыршин Никита"
"""
Задание 178Б 
Даны натуральные числа n, a1...an. 
Определить количество членов ak последовательности a1,...,an:
б) кратных 3 и не кратных 5;

https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
"""
import numpy as np
import random
from Function6 import *

def lab6(n, mas):
    res = 0 # подсчёт значений удовлетворяющих условие

    for i in range(0,n):
        if (mas[i]%3 == 0) and (mas[i]%5 != 0):
            res = res + 1

    return res



if __name__ == "__main__":
    n = int (input("Введите число n "))
    mas = np.random.randint (0, 100, n)
    res = lab6(n, mas)
    print_array(mas)
    print_res(res)
