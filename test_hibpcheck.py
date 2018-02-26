#!/usr/bin/env python3
import unittest
import hibpcheck
import os

class hibpTest(unittest.TestCase):
    '''hibpcheck tests'''

    def test(self):
        '''hibpcheck tests'''
        hibp = hibpcheck.hibpcheck('password')

        self.assertTrue(hibp.found) 
        self.assertGreater(hibp.count, 0)
    
    def test2(self):
        '''hibpcheck tests'''
        password = os.urandom(8).hex()
        hibp = hibpcheck.hibpcheck(password)

        self.assertFalse(hibp.found) 
        self.assertEqual(hibp.count, 0)