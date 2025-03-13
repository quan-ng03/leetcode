import unittest
from easy.remove_element_27 import removeElement

class TestRemoveElement(unittest.TestCase):
    def test_remove_element(self):
        nums = [3, 2, 2, 3]
        k = removeElement(nums, 3)
        self.assertEqual(k, 2)  # Expected length
        self.assertCountEqual(nums[:k], [2, 2])  # Expected elements

        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = removeElement(nums, 2)
        self.assertEqual(k, 5)  # Expected length
        self.assertCountEqual(nums[:k], [0, 1, 3, 0, 4])  # Expected elements

        nums = [2]
        k = removeElement(nums, 3)
        self.assertEqual(k, 1)  # Expected length
        self.assertCountEqual(nums[:k], [2])  # Expected elements

        nums = []
        k = removeElement(nums, 3)
        self.assertEqual(k, 0)  # Expected length
        self.assertCountEqual(nums[:k], [])  # Expected elements

if __name__ == "__main__":
    unittest.main()

