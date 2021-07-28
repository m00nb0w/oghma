#!/bin/python3

import sys


def isPalindrome(n):
    a = []
    while n != 0:
        a.append(n % 10)
        n = n // 10
    for i in range(0, len(a)):
        if (a[i] != a[-(i + 1)]):
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            t = i * j
            if t < n and isPalindrome(t):
                res = max(t, res)
            elif t > n:
                break
    print(res)
