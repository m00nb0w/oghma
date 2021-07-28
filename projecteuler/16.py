import sys


def f(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(f(pow(2, n)))
