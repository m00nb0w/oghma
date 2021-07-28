import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    t1 = 2
    t2 = 8
    res = 10
    while (t1 + 4 * t2 <= n):
        res += t1 + 4 * t2
        t = t1
        t1 = t2
        t2 = t + 4 * t1
    print(res)
