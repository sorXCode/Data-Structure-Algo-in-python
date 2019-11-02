import unittest
from recursion import factorial

class TestCases(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120, '5! should be 120')

if __name__ == "__main__":
    unittest.main()