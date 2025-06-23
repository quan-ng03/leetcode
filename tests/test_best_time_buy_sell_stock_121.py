import unittest
from easy.best_time_buy_sell_stock_121 import maxProfit


class TestMaxProfit(unittest.TestCase):
    def test(self):
        self.assertEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
