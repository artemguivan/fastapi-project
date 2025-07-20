import unittest
from calculator import Calc

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calc.add(a=1, b=2), 3)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(4, 5), 20)


