__author__ = "Монастыршин Никита"
import unittest
from Main8 import * 


class UnitTest(unittest.TestCase):
    # Test №1
    def test_lab8_1(self):
        mas = np.full((10,10),1)
        i = 2
        j = 4
        mas = lab8_matrix(mas, i, j)
        mas, sum, min, max = lab8_result(mas)
        res = [sum, min, max]
        calculation = [1494, 1 ,375]
        self.assertAlmostEqual(res, calculation)

    # Test №2
    def test_lab8_2(self):
        mas = np.full((10,10),1)
        i = 9
        j = 1
        mas = lab8_matrix(mas, i, j)
        mas, sum, min, max = lab8_result(mas)
        res = [sum, min, max]
        calculation = [1, 1 ,1]
        self.assertAlmostEqual(res, calculation)
        
        
if __name__ == "__main__":
    unittest.main()
