import unittest
from easy.delete_grtest_val_each_row_2500 import (
    deleteGreatestValue,
    deleteGreatestValueBetter,
)


class TestDeleteGreatestValEachRow(unittest.TestCase):
    def test_1(self):
        self.assertEqual(deleteGreatestValue([[1, 2, 4], [3, 3, 1]]), 8)
        self.assertEqual(deleteGreatestValue([[10]]), 10)

    def test_2(self):
        self.assertEqual(deleteGreatestValueBetter([[1, 2, 4], [3, 3, 1]]), 8)
        self.assertEqual(deleteGreatestValueBetter([[10]]), 10)


if __name__ == "__main__":
    unittest.main()
