#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

n = 20

def isPrime(number):
    for test in range(2, int(math.sqrt(number)) + 2):
        if number%test == 0:
            return False
    return True

primes = [2]

for number in range(3, n + 1):
    if isPrime(number):
        primes.append(number)

dictprimes = dict((s, 0) for s in primes)

print (dictprimes)

for nb in range(2, n + 1):
    while nb > 1:
        for key in dictprimes.keys():
            value = 0
            while nb%key == 0 and key <= nb:
                nb = nb/key
                value += 1
            if value > dictprimes[key]:
                dictprimes[key] = value

print (dictprimes)


product = 1
for key in dictprimes.keys():
    product *= key**dictprimes[key]

print ("Smallest multiple : ", product)
