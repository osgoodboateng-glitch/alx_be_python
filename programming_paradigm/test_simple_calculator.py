import unittest
from simple_calculator import  SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self):
        result = self.calc.add(5, 5)
        self.assertEqual(result, 10)
    def test_subtract(self):
        result = self.calc.subtract(8,6)
        self.assertEqual(result, 2)
    def test_multiply(self):
        result = self.calc.multiply(3, 2)
        self.assertEqual(result, 6)
    def test_divide(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(result, 2)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)
if __name__ == "__main__":
    unittest.main()      