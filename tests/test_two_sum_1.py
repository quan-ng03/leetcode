import unittest
from easy.two_sum_1 import firstApproach, secondApproach

class TestTwoSum(unittest.TestCase):
    def test_firstApproach(self):
        self.assertCountEqual(secondApproach([3, 2, 4], 6), [1, 2])
        self.assertCountEqual(secondApproach([2, 7, 11, 15], 9), [0, 1])
        self.assertCountEqual(secondApproach([3, 3], 6), [0, 1])

    def test_secondApproach(self):
        self.assertCountEqual(secondApproach([3, 2, 4], 6), [1, 2])
        self.assertCountEqual(secondApproach([2, 7, 11, 15], 9), [0, 1])
        self.assertCountEqual(secondApproach([3, 3], 6), [0, 1])

if __name__ == "__main__":
    unittest.main()
