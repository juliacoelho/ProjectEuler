# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:01:31 2017

@author: Julia
"""

def sumSquares(nb):
    total_sum = 0
    for number in range(1, nb + 1):
        total_sum += number**2
    return total_sum

def squareSum(nb):
    total_sum = 0
    for number in range(1, nb + 1):
        total_sum += number
    return total_sum**2
    
    
print (squareSum(100)-sumSquares(100))