__author__ = "Монастыршин Никита"
"""
Задание 178Б 
Даны натуральные числа n, a1...an. 
Определить количество членов ak последовательности a1,...,an:
б) кратных 3 и не кратных 5;

https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
"""
import numpy as np
from Function6 import *


if __name__ == "__main__":
    n = int (input("Введите число n "))
    mas = np.random.randint (0, 100, n) # Массив размера n со значениями от 0 до 99

    res = lab6(mas)

    print(f'Содержание массива: {mas}')
    print(f'Результат: {res}')
