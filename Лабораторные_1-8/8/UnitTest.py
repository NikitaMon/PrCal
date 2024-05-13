__author__ = "Монастыршин Никита"
import unittest
from Main8 import * 


class UnitTest(unittest.TestCase):
    def test_lab8(self):
        mas = np.full((10,10),1)
        i = 2
        j = 4
        mas = lab8_matrix(mas, i, j)
        mas, sum, min, max = lab8_result(mas, i ,j)
        res = [sum, min, max]
        calculation = [1494, 1 ,375]
        self.assertAlmostEqual(res, calculation)
        
        
if __name__ == "__main__":
    unittest.main()
