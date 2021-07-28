import sys 
import math


LIMIT = 30000


def calculateProperDivisors(a):
    res = 1 
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            res += i + (a // i)
            if i == (a // i):
                res -= i
    return res 

def preCalculate():
    d = [0] * LIMIT 
    for i in range(1, LIMIT):
        d[i] = calculateProperDivisors(i)
    return d


d = preCalculate()
resSum = 0
tests = [x for x in range(0, LIMIT)]
for n in tests:
    if n >= LIMIT:
        res = True
    else:
        res = False
        for i in range(1, n // 2 + 1):
            if (i < d[i] and (n - i) < d[n - i]):
                res = True
                
    if not res:
        resSum += n
print(resSum)
