__author__ = "Монастыршин Никита"
"""
Создайте отдельные модули (или один) с набором функций.
"""

# Лабораторная работа №5
def lab5(mas):
    """Расчёт уравнения по заданию a1/0! ... an/(n-1)!"""
    res = 0     # сумма
    fact = 1    # значение факториала
    hf = 1      # следующая переменная на которую домнажается
    n = len(mas) # размер массива

    # a = random.randint(0,10)
    # факториал 0! = 1
    #           1! = 1
    # a / (n-1)!
    for i in range(0,n):
        buf = mas[i] / fact  #заполнение массива
        fact = fact * hf    #следующее значение факториала
        hf = hf + 1         #следующая переменная для домножения
        res = res + buf  #вычисление результата
    return res

