#!/bin/python3

import sys

LIMIT = 3000100

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


def search(n, i, j):
    mid = (i + j) // 2
    if (i > j):
        return j
    if (primeList[mid] == n):
        return mid
    if (primeList[mid] > n):
        return search(n, i, mid - 1)
    if (primeList[mid] < n):
        return search(n, mid + 1, j)


primeList = generatePrimeList(LIMIT)

t = 0
sums = []
for x in primeList:
    t += x
    sums.append(t)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = search(n, 0, len(primeList))
    print(sums[i])


