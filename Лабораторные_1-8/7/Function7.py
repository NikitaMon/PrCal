__author__ = "Монастыршин Никита"

# Лабораторная №7
def lab7(n):
    """Находит сумму 1/(k**2)!, где k принимает значение от 1 до n,"""
    
    def newfact(n, fact, hf):
        """Находит факториал n при текущем факториале hf со значением fact"""
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