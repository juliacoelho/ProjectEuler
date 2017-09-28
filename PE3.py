#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(number):
    for test in range(2, int(math.sqrt(number)) + 2):
        if number%test == 0:
            return False
    return True

def nextPrime(number):
    number +=1
    if isPrime(number):
        return number
    return nextPrime(number)

n = 600851475143
prime = 2

while n>1:
    while n%prime == 0 and prime <= n:
        n = n/prime
        print (prime)
    prime = nextPrime(prime)
