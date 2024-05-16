__author__ = "Монастыршин Никита"
import unittest
from Function6 import * 


class UnitTest(unittest.TestCase):
    # Test №1
    def test_lab6_1(self):
        mas = [5,10,9,6,3]

        res = lab6(mas)
        calculation = 3

        self.assertAlmostEqual(res, calculation)
    
    # Test №2
    def test_lab6_2(self):
        mas = [4,5,8,7,0]

        res = lab6(mas)
        calculation = 0

        self.assertAlmostEqual(res, calculation)

    # Test №3
    def test_lab6_3(self):
        mas = [5.1,10.1,9.1,6.1,3.3]

        res = lab6(mas)
        calculation = 0

        self.assertAlmostEqual(res, calculation)
        
        
if __name__ == "__main__":
    unittest.main()
