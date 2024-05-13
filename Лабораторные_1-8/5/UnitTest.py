__author__ = "Монастыршин Никита"
import unittest
#from Main5 import * 
#import Main5 

class UnitTest(unittest.TestCase):
    def test_lab5(self):
        # Test
        n = 5 # число элементов
        mas = [1, 2, 3, 4, 5] # создание массива с определёнными значениями

        calculation = 1/1 + 2/1 + 3/2 + 4/6 + 5/24 # расчёт по формуле в ручную
        
        res = 0     #сумма
        fact = 1    #значение факториала
        hf = 1      #следующая переменная на которую домнажается

        # a = random.randint(0,10)
        # факториал 0! = 1
        #           1! = 1
        # a / (n-1)!
        for i in range(0,n):
            buf = mas[i] / fact  #заполнение массива
            fact = fact * hf    #следующее значение факториала
            hf = hf + 1         #следующая переменная для домножения
            res = res + buf  #вычисление результата

        # проверка результата алгоритма и подсчёта вручную
        self.assertAlmostEqual(calculation,res)
        
        
if __name__ == "__main__":
    unittest.main()
