#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:01:41 2019

@author: qcat
"""

import unittest

from fizzbuzz import FzBz

class TestFzBz(unittest.TestCase):

    def test_fizz_3mul(self):
        # 3的倍数
        self.assertEqual(FzBz(3,5,9).fizz_buzz(),"Fizz")
        
    def test_fizz_3(self):
        # 含有3的数
        self.assertEqual(FzBz(3,5,13).fizz_buzz(),"Fizz")
        
    def test_buzz_5mul(self):
        # 5的倍数
        self.assertEqual(FzBz(3,5,70).fizz_buzz(),"Buzz")
        
    def test_buzz_5(self):
        # 含有5的数
        self.assertEqual(FzBz(3,5,52).fizz_buzz(),"Buzz")
        
    def test_fizzbuzz_3_5_mul(self):
        # 3 & 5的公倍数
        self.assertEqual(FzBz(3,5,90).fizz_buzz(),"FizzBuzz")
        
    def test_fizz_3_5(self):
        # 同时含有3和5的数
        self.assertEqual(FzBz(3,5,53).fizz_buzz(),"FizzBuzz")
        
if __name__ == '__main__':
    unittest.main()
        

