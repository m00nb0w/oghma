import math

n = int(input().strip())
res = 0

f = [math.factorial(x) for x in range(10)]
for i in range(10, n):
    t = sum([f[int(x)] for x in str(i)])
    if t == i:
        res += i

print(res)
