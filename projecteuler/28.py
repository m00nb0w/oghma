"""

Algorithm: 
    * x = n // 2
    * f(x) is the sum of 4 corner at the 2x + 1 ring (nth ring) => f(x) = 4(2x + 1)^2 - 6(2x + 1) + 6
    * Using the Ken Ward's algorithm to find the formation for the sum of f(x), we have:
        H(k) = sum(x: 1->k) f(x) = 16/3 * k^3 + 10 * k^2 + 26/3 * k + 1

"""

import sys
import math


MODULE = pow(10, 9) + 7


tests = int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    n = n // 2
    print(((16 * pow(n, 3) + 30 * pow(n, 2) + 26 * n) // 3 + 1) % MODULE)
