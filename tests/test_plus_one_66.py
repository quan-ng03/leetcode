import unittest
from easy.plus_one_66 import plusOne, plusOneBetter

class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual(plusOne([4,3,2,1]), [4,3,2,2])
        self.assertEqual(plusOne([9,9,9,9,9,9,9,9]), [1,0,0,0,0,0,0,0,0])
    def test_plus_one_better(self):
        self.assertEqual(plusOneBetter([4,3,2,1]), [4,3,2,2])
        self.assertEqual(plusOneBetter([9,9,9,9,9,9,9,9]), [1,0,0,0,0,0,0,0,0])
if __name__ == "__main__":
    unittest.main()
