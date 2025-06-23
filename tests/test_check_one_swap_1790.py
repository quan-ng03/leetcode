import unittest
from easy.check_one_swap_1790 import areAlmostEqual


class TestSwap(unittest.TestCase):
    def test(self):
        self.assertEqual(areAlmostEqual("bank", "kanb"), True)
        self.assertEqual(areAlmostEqual("attack", "defend"), False)
        self.assertEqual(areAlmostEqual("kelb", "kelb"), True)


if __name__ == "__main__":
    unittest.main()
