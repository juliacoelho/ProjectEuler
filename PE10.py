# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 00:21:31 2017

@author: Julia
"""
import math

def isPrime(nb):
    for number in range(2, int(math.sqrt(nb)) + 2):
        if nb%number == 0:
            return False
    return True

def sumPrimes(nb):
    sum_ = 2
    for number in range(3, nb):
        if isPrime(number):
            sum_ += number
    print (sum_)

sumPrimes(2000000)