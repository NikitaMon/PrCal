__author__ = "Монастыршин Никита"
"""
Задание 136И
Даны натуральное число n, действительные числа a1,..., an. Вычислить:

https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
"""

import numpy as np
from Function5 import *


if __name__ == "__main__":
    print("Лабораторная №5")
    n = int (input("Введите число n "))
    mas = np.random.randint (0, 10, n) # создание массива с числами от 0 до 9 в количестве n
    res = lab5(mas)
    print(f"Результат = {res:.3f}")

