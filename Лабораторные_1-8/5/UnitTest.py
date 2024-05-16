__author__ = "Монастыршин Никита"
import unittest
from Function5 import * 


class UnitTest(unittest.TestCase):
    def test_lab5_1(self):
        # Test №1
        mas = [1, 2, 3, 4, 5] # создание массива с определёнными значениями
        calculation = 1/1 + 2/1 + 3/2 + 4/6 + 5/24 # расчёт по формуле в ручную
        res = lab5(mas)
        # проверка результата алгоритма и подсчёта вручную
        self.assertAlmostEqual(calculation,res)

    def test_lab5_2(self):
        # Test №2
        mas = [1.5, 1.4, 1.3, 1.2, 1.1] # создание массива с определёнными значениями
        calculation = 1.5/1 + 1.4/1 + 1.3/2 + 1.2/6 + 1.1/24 # расчёт по формуле в ручную
        res = lab5(mas)
        # проверка результата алгоритма и подсчёта вручную
        self.assertAlmostEqual(calculation,res)

    def test_lab5_3(self):
        # Test №3
        mas = [0, 0, 0, 0, 0] # создание массива с определёнными значениями
        calculation = 0/1 + 0/1 + 0/2 + 0/6 + 0/24 # расчёт по формуле в ручную
        res = lab5(mas)
        # проверка результата алгоритма и подсчёта вручную
        self.assertAlmostEqual(calculation,res)
        
        
if __name__ == "__main__":
    unittest.main()
