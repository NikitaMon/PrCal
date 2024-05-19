__author__ = "Монастыршин Никита"
"""
Задание 136И
Даны натуральное число n, действительные числа a1,..., an. Вычислить:

https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
"""

import numpy as np
from Function5 import *

import textwrap
import argparse

parser = argparse.ArgumentParser(prog='Main5.py',
                                 description='Вычислить по формуле a1/0! + a2/1! + ... + an/(n-1)!',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\
                                                                Лабораторная №5
                                        Задание 136И
                                            Даны натуральное число n, действительные числа a1,..., an. Вычислить:
                                            https://ivtipm.github.io/Programming/Glava06/index06.htm#z136''')
                                )

#parser.add_argument("n", type=int, choices=range(1, 100), help='Колличество элементов по которым будет происходить расчёт.')
parser.add_argument("n", type=int, help='Колличество элементов по которым будет происходить расчёт.')


args = parser.parse_args()
mas = np.random.randint (0, 10, args.n) # создание массива с числами от 0 до 9 в количестве n
res = lab5(mas)
print(f"Результат = {res:.3f}")

