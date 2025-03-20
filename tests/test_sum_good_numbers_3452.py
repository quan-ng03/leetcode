import unittest
from easy.sum_good_numbers_3452 import sumOfGoodNumbers

class TestSumGoodNumbers(unittest.TestCase):
    def test(self):
        self.assertEqual(sumOfGoodNumbers([1,3,2,1,5,4],2), 12)
        self.assertEqual(sumOfGoodNumbers([2,1],1), 2)
if __name__ == "__main__":
    unittest.main()