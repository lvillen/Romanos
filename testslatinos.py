import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])

    def test_descomponer_solo_enteros(self):
        self.assertRaises(SyntaxError, descomponer, 1987.0)

    def test_convertir_1987(self):
        self.assertEqual(convertir([1, 9, 8, 7]), 'MCMLXXXVII')

    def test_convertir_987(self):
        self.assertEqual(convertir([9, 8, 7]), 'CMLXXXVII')


if __name__ == '__main__':
    unittest.main()
