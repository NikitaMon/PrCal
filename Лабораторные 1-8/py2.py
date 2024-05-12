__author__ = "Монастыршин Никита"

"""
Задача 37 
Даны действительные числа a, b, c. 
Удвоить эти числа, если a ≥ b ≥ c, 
и заменить их абсолютными значениями, если это не так.

https://ivtipm.github.io/Programming/Glava02/index02.htm#z37
"""
import math

a = float (input("Введите число a "))
b = float (input("Введите число b "))
c = float (input("Введите число c "))

if a >= b >= c:
	a = a*2
	b = b*2
	c = c*2
else:
	a=abs(a)
	b=abs(b)
	c=abs(c)

print (f"a = {a:.3f}") 
print (f"b = {b:.3f}") 
print (f"c = {c:.3f}") 
