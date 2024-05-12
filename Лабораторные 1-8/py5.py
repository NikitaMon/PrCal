__author__ = "Монастыршин Никита"
"""
Задание 136И
Даны натуральное число n, действительные числа a1,..., an. Вычислить:

https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
"""
import array
import random

n = int (input("Введите число n "))

res = 0     #сумма
fact = 1    #значение факториала
hf = 1      #следующая переменная на которую домнажается

# a = random.randint(0,10)
# факториал 0! = 1
#           1! = 1
# a / (n-1)!
for i in range(0,n):
    buf = random.randint(0,10) / fact  #заполнение массива
    fact = fact * hf    #следующее значение факториала
    hf = hf + 1         #следующая переменная для домножения
    res = res + buf  #вычисление результата


print(f"Результат = {res:.3f}")

