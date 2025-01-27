import unittest
from easy.valid_paren_20 import isValid

class TestContainsDuplicate(unittest.TestCase):
    def test(self):
        self.assertEqual(isValid("()"), True)
        self.assertEqual(isValid("()[]{}"), True)
        self.assertEqual(isValid("(]"), False)
        self.assertEqual(isValid("([])"), True)
if __name__ == "__main__":
    unittest.main()