#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:51:07 2019

@author: qcat
"""

class FzBz:
    def __init__(self,num1,num2,num):
        self.num1 = num1
        self.num2 = num2
        self.num = num
    def fizz_buzz(self):
        # num1 & num2
        if (self.num % self.num1 == 0 or str(self.num1) in str(self.num)) and (self.num % self.num2 == 0 or str(self.num2) in str(self.num)):
            return "FizzBuzz"
            # num1
        elif self.num % self.num1 == 0 or str(self.num1) in str(self.num):
            return "Fizz"
        elif self.num % self.num2 == 0 or str(self.num2) in str(self.num):
            return "Buzz"
        else:
            return self.num
        
for i in range(1,101):
    fzbz = FzBz(3,5,i)
    print(fzbz.fizz_buzz())