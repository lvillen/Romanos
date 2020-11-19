import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])

    def test_convertir_1987(self):
        self.assertEqual(convertir([1, 9, 8, 7]), 'MCMLXXXVII')

    def test_convertir_987(self):
        self.assertEqual(convertir([9, 8, 7]), 'CMLXXXVII')
    
    def test_entero_a_romano(self):
        self.assertRaises(SyntaxError, entero_a_romano, 1987.0)
        self.assertRaises(OverflowError, entero_a_romano, 0)
        self.assertRaises(OverflowError, entero_a_romano, 4000)
        self.assertEqual(entero_a_romano(1987), 'MCMLXXXVII')

if __name__ == '__main__':
    unittest.main()
