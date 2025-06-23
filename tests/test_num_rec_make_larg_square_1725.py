import unittest
from easy.num_rec_make_larg_square_1725 import countGoodRectangles


class TestCountGoodRecs(unittest.TestCase):
    def test(self):
        self.assertEqual(countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]), 3)
        self.assertEqual(countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]), 3)


if __name__ == "__main__":
    unittest.main()
