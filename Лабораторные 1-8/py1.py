__author__ = 'Монастыршин Никита'
""" Задача 8
	Определить периметр правильного n-угольника, 
	описанного около окружности радиуса r.

	https://ivtipm.github.io/Programming/Glava01/index01.htm#z8
"""

import math


r = float ( input ("Введите радиус\n")) 


n = int ( input ("Введите число углов\n"))


res = 2 * r * n * math.tan(math.pi / n)	
print (f"Периметр {res:.3f}") 