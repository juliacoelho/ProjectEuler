#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def isPali(number):
    if str(number) == str(number)[::-1]:
        return True
    return False

pali = []

for a in range(100, 1000):
    for b in range(100, 1000):
        product = a*b
        if isPali(product):
            pali.append(product)

print (pali)
print ("Biggest : ", max(pali))
