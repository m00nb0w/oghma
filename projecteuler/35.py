import math
import sys

LIMIT = pow(10, 6) + 17

def generatePrime(n):
    isPrime = [True] * LIMIT
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, n):
        if isPrime[i]:
            for j in range(2, n // i):
                isPrime[i * j] = False
    return isPrime

def convert(s):
    return (s[1:] + s[0])

n = int(input().strip())
isPrime = generatePrime(LIMIT)
res = 0
for i in range(2, n):
    t = str(i)
    flag = True
    for _ in range(len(str(i))):
        if not isPrime[int(t)]:
            flag = False
            break
        t = convert(t)
    if flag:
        res += 1
        
print(res)
    
