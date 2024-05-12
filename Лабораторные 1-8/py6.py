__author__ = "Монастыршин Никита"
"""
Задание 178Б 
Даны натуральные числа n, a1...an. 
Определить количество членов ak последовательности a1,...,an:
б) кратных 3 и не кратных 5;

https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
"""
import array
import random

n = int (input("Введите число n "))
res = 0
mas = [0]*n


for i in range(0,n):
    mas[i] =  random.randint(0, 100)
    if (mas[i]%3 == 0) and (mas[i]%5 != 0):
        res = res + 1

print(f'Содержание массива: {mas}')
print(f'Результат: {res}')
