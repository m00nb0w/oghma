import sys
from functools import lru_cache


LIMIT = 5 * pow(10, 6) + 10

d = {}

# @lru_cache(None)
def f(n):
    if n in d:
        return d[n]
    if (n == 1 or n == 0):
        return 0
    if (n % 2 == 1):
        t = f(3 * n + 1) + 1
        if (n < LIMIT):
            d[n] = t
        return t
    else:
        t = f(n // 2) + 1
        if (n < LIMIT):
            d[n] = t
        return t
    

maxList = []
maxVal = 0
res = 0
for i in range(0, 5000100):
    if maxVal <= f(i):
        res = i
        maxVal = f(i)
    # print(i, maxVal, f(i))
    maxList.append(res)
    
t = int(input().strip())
for _ in range(0, t):
    n = int(input().strip())
    print(maxList[n])
