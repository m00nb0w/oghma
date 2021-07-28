import sys

def countDigit(n):
    res = 0
    while n != 0:
        n = n // 10
        res += 1
    return res

n = int(input().strip())
res = 0
for _ in range(0, n):
    t = int(input().strip())
    res += t
print(res // pow(10, countDigit(res) - 10))
