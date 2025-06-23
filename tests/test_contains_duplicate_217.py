import unittest
from easy.contains_duplicate_217 import containsDuplicate


class TestContainsDuplicate(unittest.TestCase):
    def test(self):
        self.assertEqual(containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
        self.assertEqual(containsDuplicate([1, 2, 3, 4]), False)


if __name__ == "__main__":
    unittest.main()
