__author__ = "Монастыршин Никита"
import unittest
from Main6 import * 


class UnitTest(unittest.TestCase):
    def test_lab6(self):
        n = 5
        mas = [5,10,9,6,3]
        res = lab6(n,mas)

        calculation = 3

        self.assertAlmostEqual(res, calculation)
        
        
if __name__ == "__main__":
    unittest.main()
