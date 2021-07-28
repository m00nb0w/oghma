#!/bin/python3

import sys


LIMIT = 1000010


def generatePrimeList(n):
    primeList = []
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n):
        if (isPrime[i]):
            primeList.append(i)
            for j in range(2, n // i):
                isPrime[i * j] = False
    return primeList

primeList = generatePrimeList(LIMIT)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeList[n - 1])
