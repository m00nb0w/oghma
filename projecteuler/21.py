import sys
import math


LIMIT = pow(10, 5) + 10


def calculateProperDivisors(a):
    res = 1 
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            res += i + (a // i)
    return res 

def preCalculate():
    d = [0] * LIMIT 
    for i in range(1, LIMIT):
        d[i] = calculateProperDivisors(i)
        
    sums = [0] * LIMIT
    t = 0
    for i in range(2, LIMIT):
        sums[i] = t
        if (d[i] >= LIMIT and i != d[i]):
            temp = calculateProperDivisors(d[i])
            if (i == temp):
                t += i
        elif i == d[d[i]] and i != d[i]:
            t += i
    return sums
    

sums = preCalculate()
tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    print(sums[n])
    
