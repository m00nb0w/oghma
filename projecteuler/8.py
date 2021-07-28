#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    numberList = [int(s) for s in num]
    res = 0
    for i in range(0, n - k + 1):
        t = 1
        for j in range(i, i + k):
            t = t * numberList[j]
        res = max(res, t)
    print(res)
