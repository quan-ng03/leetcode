import unittest
from easy.maximum_achievable_number_2769 import theMaximumAchievableX

class TestMaxAchieveNum(unittest.TestCase):
    def test(self):
        self.assertEqual(theMaximumAchievableX(4, 1), 6)
        self.assertEqual(theMaximumAchievableX(3, 2), 7)
if __name__ == "__main__":
    unittest.main()
