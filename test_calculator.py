import unittest
import math
from calculator_logic import evaluate_basic, evaluate_scientific

class TestBasicCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate_basic("3+5"), 8)

    def test_invalid_expression(self):
        self.assertEqual(evaluate_basic("3+*2"), "Error")

class TestScientificCalculator(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(evaluate_scientific("sin", 30), 0.5, places=5)

    def test_invalid_func(self):
        self.assertEqual(evaluate_scientific("unknown", 10), "Error")

if __name__ == "__main__":
    unittest.main()
