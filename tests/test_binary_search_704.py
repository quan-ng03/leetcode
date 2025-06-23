import unittest
from easy.binary_search_704 import search


class TestMaxAchieveNum(unittest.TestCase):
    def test(self):
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
