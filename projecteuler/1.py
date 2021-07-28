import sys

def solution(n):
    t1 = (n - 1) // 3
    t2 = (n - 1) // 5
    t3 = (n - 1) // 15
    res = ((t1 + 1) * t1 // 2) * 3 + ((t2 * (t2 + 1)) // 2) * 5 - ((t3 * (t3 + 1)) // 2) * 15
    return res

print("Enter number of test cases: ")
t = int(input().strip())
for a0 in range(t):
    print("Enter number: ")
    n = int(input().strip())
    print(solution(n))
