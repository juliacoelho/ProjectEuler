def nextFibo(n1, n2):
    return (n1 + n2)

n1 = 1
n2 = 2
total = 2

while (nextFibo(n1, n2) < 4000001):
    temp = nextFibo(n1, n2)
    if temp%2 == 0:
        total += temp
    n1 = n2
    n2 = temp

print (total)
