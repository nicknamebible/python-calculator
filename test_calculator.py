import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_add_3(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()