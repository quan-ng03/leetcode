import unittest
from easy.counting_bits_338 import countBits1, countBits2

class TestcountBits1(unittest.TestCase):
    def test(self):
        self.assertEqual(countBits1(2), [0,1,1])
        self.assertEqual(countBits1(5), [0,1,1,2,1,2])
        self.assertEqual(countBits1(100), [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,2,3,3,4,3])
class TestcountBits2(unittest.TestCase):
    def test(self):
        self.assertEqual(countBits2(2), [0,1,1])
        self.assertEqual(countBits2(5), [0,1,1,2,1,2])
        self.assertEqual(countBits2(100), [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5,2,3,3,4,3,4,4,5,3,4,4,5,4,5,5,6,2,3,3,4,3])
if __name__ == "__main__":
    unittest.main()