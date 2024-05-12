__author__ = "Монастыршин Никита"
"""
Задание 335В 
Дано натуральное число n. 
Вычислить:

https://ivtipm.github.io/Programming/Glava10/index10.htm#z335
"""

hf = 1 #переменная использующаяся как глобальная в newfact

#расчёт факториала от hf до n(k**2) по формуле задания
def newfact(n,fact):
    global hf
    for i in range(hf,n+1):
        fact = fact * hf
        hf = hf + 1
    return fact


fact = 1
res = 0
n = int (input("Введите число n "))

for k in range(1,n+1):
    fact = newfact(k*k,fact)
    res = res + 1 / (fact*(k**2))
 

print(f"Результат = {res:.3f}")
