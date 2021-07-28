n, m = input().strip().split(" ")
n, m = int(n), int(m)

res = 0
for i in range(2, n):
    s = set()
    c = ""
    for k in range(1, 10):
        t = i * k
        c = c + str(t)
        flag = False
        for x in str(t):
            if int(x) > m or int(x) in s or int(x) == 0:
                flag = True
                break
            else:
                s.add(int(x))
        if flag:
            break
        if len(s) == m:
            res = max(res,int(c))
            break

print(res)
