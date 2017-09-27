# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:57:27 2017

@author: Julia
"""

# a vai de 1 ate 995

def isTriple(a, b, c):
    return (a**2 + b**2 == c**2)

for a in range(1, 996):
    for b in range(a + 1, 997):
        for c in range(b + 1, 998):
            if a+b+c == 1000:
                if isTriple(a, b, c):
                    print (a * b * c)