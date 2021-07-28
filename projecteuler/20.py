import sys
import math

tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    print(sum(map(int, str(math.factorial(n)))))
