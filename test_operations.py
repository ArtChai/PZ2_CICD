
import unittest

from operations import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(6, 7, "+"), 13)

    def test_subtraction(self):
        self.assertEqual(calculate(2, 1, "-"), 1)

    def test_multiplication(self):
        self.assertEqual(calculate(3, 4, "*"), 12)

if __name__ == "__main__":
    unittest.main()
