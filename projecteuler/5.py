#!/bin/python3

import sys


t = int(input().strip())

primes = [2]
primeCount = [1]

for a0 in range(t):
    n = int(input().strip())
    primes = []
    primeCount = []
    for i in range(2, n + 1):
        tempCount = []
        t = i
        for prime in primes:
            c = 0
            while (t % prime == 0):
                t = t // prime
                c += 1
            tempCount.append(c)
        if (t == i):
            primes.append(i)
            primeCount.append(1)
        else:
            for j in range(0, len(primes)):
                primeCount[j] = max(primeCount[j], tempCount[j])
    res = 1
    for i in range(0, len(primes)):
        res *= pow(primes[i], primeCount[i])
    print(res)
            
