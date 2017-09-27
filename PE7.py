# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:31:50 2017

@author: Julia
"""
import math

def isPrime(nb):
    for number in range(2, int(math.sqrt(nb)) + 2):
        if nb%number == 0:
            return False
    return True

def nextPrime(nb):
    nb += 1
    if isPrime(nb):
        return nb
    return nextPrime(nb)


primes = [2]

while len(primes) < 10001:
    primes.append(nextPrime(primes[-1]))

print (primes[-1])