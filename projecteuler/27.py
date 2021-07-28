import sys 
import math


LIMIT = pow(10, 6) + 15


def generatePrimeList():
    isPrime = [True] * LIMIT 
    isPrime[0] = isPrime[1] = False
    for i in range(2, LIMIT):
        if (isPrime[i]):
            for j in range(2, LIMIT // i):
                isPrime[i * j] = False
    return isPrime

isPrime = generatePrimeList()    
n = int(input().strip())

resA = 0
resB = 0
maxVal = 0
for b in range(2, n + 1):
    for a in range(-n, n + 1):
        i = 0
        while True:
            t = pow(i, 2) + a * i + b
            if (isPrime[t]):
                i += 1
            else:
                break
        if i > maxVal:
            resA = a 
            resB = b
            maxVal = i

print(resA * resB) 

