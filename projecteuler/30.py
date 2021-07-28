import sys 
import math


LIMIT = pow(10, 6) + 17


def calculate(a, n):
    s = 0
    t = a
    while a != 0:
        s += pow(a % 10, n)
        a = a // 10
    return s == t
    

n = int(input().strip())
res = 0
for i in range(2, LIMIT):
    if calculate(i, n):
        res += i
    
print(res)
