import sys
import math


LIMIT = 5 * pow(10, 4) + 15


def preCalculate():
    d = [1]
    t1 = 1
    t2 = 1
    count = 1
    cap = 10
    for i in range(3, LIMIT):
        t = (t1 + t2)
        if (t >= cap):
            count += 1
            d.append(i)
            cap *= 10
        t1 = t2
        t2 = t
        
    return d
        

d = preCalculate()
tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
        print(d[n - 1])
