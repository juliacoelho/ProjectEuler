import math, itertools

# Find primes up to :
n = 500000

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

#print (dictprimes)

def getPrimeFactors(nb):
    myDict = dictprimes
    while nb > 1:
        for key in myDict.keys():
            value = 0
            while nb%key == 0 and key <= nb:
                nb = nb/key
                value += 1
            myDict[key] = value
    return myDict

"""
def combineValues(list_):
    divisors = []
    for element in itertools.product(*list_):
        divisors.append(element)
    return divisors

def getDivisors(nb):
    if nb == 1:
        return [1]
    dict_ = getPrimeFactors(nb)
    list_ = []
    for key in dict_.keys():
        if dict_[key] > 0:
            list_.append([])
            for exp in range(dict_[key] + 1):
                list_[-1].append(key**exp)
    divisorsFactors = combineValues(list_)
    divisors = []
    for set_ in divisorsFactors:
        product = 1
        for element in set_:
            product *= element
        divisors.append(product)
    return divisors
"""

def getNbDivisors(nb):
    product = 1
    for element in getPrimeFactors(nb).values():
        product *= (element + 1)
    return product

def sumOfN(nb):
    return (nb+nb**2)/2

i = 1
while getNbDivisors(sumOfN(i)) < 500:
    i+=1
    print("   ", getNbDivisors(sumOfN(i)))
    print (sumOfN(i))
print("Brasil")







