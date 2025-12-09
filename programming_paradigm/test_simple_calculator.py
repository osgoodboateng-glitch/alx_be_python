import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Create a calculator instance before each test
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Explicitly test addition
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 6), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)

if __name__ == "__main__":
    unittest.main()
