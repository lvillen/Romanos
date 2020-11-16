import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_single_symbol(self):
        self.assertEqual(romano_a_entero('M'), 1000)
        self.assertEqual(romano_a_entero('D'), 500)
        self.assertEqual(romano_a_entero('C'), 100)
        self.assertEqual(romano_a_entero('L'), 50)
        self.assertEqual(romano_a_entero('X'), 10)
        self.assertEqual(romano_a_entero('V'), 5)
        self.assertEqual(romano_a_entero('I'), 1)

        self.assertRaises(ValueError, romano_a_entero, 'Z')
        self.assertRaises(ValueError, romano_a_entero, 23)

    def test_varios_simbolos(self):
        self.assertEqual(romano_a_entero('MMM'), 3000)
        self.assertEqual(romano_a_entero('CC'), 200)
        self.assertEqual(romano_a_entero('III'), 3)
        self.assertEqual(romano_a_entero('XX'), 20)

    def test_errores_repes(self):
        self.assertRaises(OverflowError, romano_a_entero, 'MMMM') #OverflowError('Demasiados tipos de M')
        self.assertRaises(OverflowError, romano_a_entero, 'VV')

    def test_repes_variadas(self):
        self.assertEqual(romano_a_entero('MMLXXIII'), 2073)

    def test_restas(self):
        self.assertEqual(romano_a_entero('IV'), 4)
        self.assertEqual(romano_a_entero('IX'), 9)
        self.assertEqual(romano_a_entero('MCMLXXXIV'), 1984)
    
    def test_restas_errores(self):
        self.assertRaises(ValueError, romano_a_entero, 'IC')

'''
    def test_por_solucionar(self):
        self.assertRaises(ValueError, romano_a_entero, 'MMCMM') 
        self.assertRaises(ValueError, romano_a_entero, 'IIX') 
'''


if __name__ == '__main__':
    unittest.main()