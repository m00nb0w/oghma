import sys

tests = int(input().strip())
for _ in range(tests):
    a = []
    n = int(input().strip())
    for _ in range(n):
        a.append([int(s) for s in input().strip().split(" ")])
    
    dx = [-1, 0]
    f = []
    f.append(a[0])
    res = 0
    for i in range(1, len(a)):
        f.append([])
        for j in range(0, len(a[i])):
            t = 0 
            for k in range(2):
                if (j + dx[k] >= 0 and j + dx[k] < len(f[i - 1])):
                    t = max(t, f[i - 1][j + dx[k]])
            f[i].append(t + a[i][j])
            res = max(res, t + a[i][j])
    print(res)
