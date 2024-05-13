__author__ = "Монастыршин Никита"
"""
Задание 335В 
Дано натуральное число n. 
Вычислить:

https://ivtipm.github.io/Programming/Glava10/index10.htm#z335
"""
from Function7 import *

def lab7(n):
    #расчёт факториала от hf до n(k**2) по формуле задания
    def newfact(n, fact, hf):
        for i in range(hf,n+1):
            fact = fact * hf
            hf = hf + 1
        return fact, hf

    hf = 1 #переменная факториала
    fact = 1 # значение факториала
    res = 0

    # формула задачи
    for k in range(1,n+1):
        fact, hf = newfact(k*k,fact,hf)
        res = res + 1 / fact

    return res


if __name__ == "__main__":
    n = int (input("Введите число n "))
    res = lab7(n)
    print_doubleres(res)
