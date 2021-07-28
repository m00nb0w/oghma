import sys
import math

MODULE = pow(10, 9) + 7

t = int(input().strip())
for _ in range(t):
    m, n = input().strip().split(" ")
    m, n = [int(m), int(n)]
    print((math.factorial(m + n) // (math.factorial(n) * math.factorial(m))) % MODULE)
    
