from functools import lru_cache
import sys


COINS = [1, 2, 5, 10, 20, 50, 100, 200]
MOD = pow(10, 9) + 7
LIMIT = pow(10, 5) + 10


def preCalculate(n):
    f = {}
    f[(0, 0)] = 1
    for i in range(0, 8):
        for j in range(0, n + 1):
            t = f.get((i, j), 0)
            x = f.get((i, j + COINS[i]), 0)
            f[(i, j + COINS[i])] = (x + t) % MOD
            x = f.get((i + 1, j), 0)
            f[(i + 1, j)] = (x + t) % MOD
    
    return f
            
    
f = preCalculate(LIMIT)

tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    print(f[8, n])

