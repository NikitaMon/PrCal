__author__ = "Монастыршин Никита"
import unittest
from Main7 import * 


class UnitTest(unittest.TestCase):
    def test_lab7(self):
        res = lab7(5)
        calculation = 1/1 + 1/24 + 1/362880 + 1/20922789888000 + 1/15511210043330985984000000
        self.assertAlmostEqual(res,calculation)
        
        
if __name__ == "__main__":
    unittest.main()
