#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = -1
    for a in range(1, n // 3 + 1):
        b = (n - (a * n) / (n - a)) / 2
        if (int(b) == b):
            b = int(b)
            c = n - a - b
            if a < b and b < c:
                res = max(res, a * b * c)
    print(res)
