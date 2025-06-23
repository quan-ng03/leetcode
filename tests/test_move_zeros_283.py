import unittest
from easy.move_zeros_283 import moveZeroes


class TestmoveZeroes(unittest.TestCase):
    def test(self):
        self.assertEqual(moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(moveZeroes([0]), [0])


if __name__ == "__main__":
    unittest.main()
