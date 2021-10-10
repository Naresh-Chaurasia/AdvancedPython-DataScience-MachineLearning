import unittest
from Calculator import add

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        summation = add(10,20)
        self.assertEqual(summation, 40)

unittest.main()
