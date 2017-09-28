def isMultiple3(n):
    return ((n%3 == 0) and (n > 0))

def isMultiple5(n):
    return ((n%5 == 0) and (n > 0))

total = 0
for number in range(1,1000):
    if (isMultiple3(number) or isMultiple5(number)):
        print (number)
        total += number
print ("total : ", total)
