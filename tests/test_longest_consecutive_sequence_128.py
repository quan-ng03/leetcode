import unittest
from medium.longest_consecutive_sequence_128 import longestConsecutive


class TestContainsDuplicate(unittest.TestCase):
    def test(self):
        self.assertEqual(
            longestConsecutive([100, 4, 200, 1, 3, 2]),
            4,
        )
        self.assertEqual(
            longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
            9,
        )
        self.assertEqual(
            longestConsecutive([1, 0, 1, 2]),
            3,
        )


if __name__ == "__main__":
    unittest.main()
