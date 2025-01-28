'''
This is a set of Unit Tests for the `convert` module
'''

import unittest
from convert import *

class TestConvert(unittest.TestCase):
    '''Unit Tests for each function in the convert module'''
    def test_c_to_f(self):
        # accepts numbers as (str, int, float)
        self.assertAlmostEqual(c_to_f('c_to_f',['37.6']), 99.68, places=4)
        self.assertAlmostEqual(c_to_f('c_to_f',[37.6]), 99.68, places=4)
        self.assertAlmostEqual(c_to_f('c_to_f',['-12']), 10.4, places=4)
        self.assertAlmostEqual(c_to_f('c_to_f',[-12]), 10.4, places=4)

        # only accepts numbers
        with self.assertRaises(ValueError):
            c_to_f('c_to_f', 'haha')
        with self.assertRaises(ValueError):
            c_to_f('c_to_f', 'Twelve')

    def test_f_to_c(self):
        # accepts numbers as (str, int, float)
        self.assertAlmostEqual(f_to_c('f_to_c',['55.4']), 13.0, places=4)
        self.assertAlmostEqual(f_to_c('f_to_c',[55.4]), 13.0, places=4)
        self.assertAlmostEqual(f_to_c('f_to_c',['-6']), -21.1111, places=4)
        self.assertAlmostEqual(f_to_c('f_to_c',[-6]), -21.1111, places=4)

        # only accepts numbers
        with self.assertRaises(ValueError):
            f_to_c('f_to_c', 'haha')
        with self.assertRaises(ValueError):
            f_to_c('f_to_c', 'Twelve')

    def test_usd_to_thb(self):
        # accepts numbers as (str, int, float)
        self.assertAlmostEqual(usd_to_thb('USD_to_THB',['1']), 33.9, places=1)
        self.assertAlmostEqual(usd_to_thb('USD_to_THB',[1]), 33.9, places=1)
        self.assertAlmostEqual(usd_to_thb('USD_to_THB',['5.55']), 188.4, places=1)
        self.assertAlmostEqual(usd_to_thb('USD_to_THB',[5.55]), 188.4, places=1)

        # only accepts numbers
        with self.assertRaises(ValueError):
            usd_to_thb('usd_to_thb', 'haha')
        with self.assertRaises(ValueError):
            usd_to_thb('usd_to_thb', 'Twelve')

    def test_thb_to_usd(self):
        # accepts numbers as (str, int, float)
        self.assertAlmostEqual(thb_to_usd('THB_to_USD',['1']), 0.03, places=2)
        self.assertAlmostEqual(thb_to_usd('THB_to_USD',[1]), 0.03, places=2)
        self.assertAlmostEqual(thb_to_usd('THB_to_USD',['5555.50']), 163.6, places=1)
        self.assertAlmostEqual(thb_to_usd('THB_to_USD',[5555.50]), 163.6, places=1)

        # only accepts numbers
        with self.assertRaises(ValueError):
            thb_to_usd('thb_to_usd', 'haha')
        with self.assertRaises(ValueError):
            thb_to_usd('thb_to_usd', 'Twelve')

if __name__ == '__main__':
    # Run Tests
    # TestConvert inherits unittest.main()
    unittest.main()