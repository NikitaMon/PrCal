__author__ = "Монастыршин Никита"
"""
Задание 115А 
Дано натуральное число n. Вычислить:

https://ivtipm.github.io/Programming/Glava04/index04.htm#z115
"""

n = int (input("Введите число n "))
res = 0

for i in range(1,n+1):
    res = res + 1/i
    print(i)

print (f"Результат {res:.3f}") 

