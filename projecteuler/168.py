import sys

m = int(input().strip())
res = 0
        
for i in range(2, m + 1):
    for b in range(1, 10):
        for t in range(1, 10):
            x = b * (pow(10, i - 1) - t) 
            y = 10 * t - 1
            if (x % y == 0 and len(str(x // y)) == i - 1):
                res += ((x // y) * 10 + b) % 100000
                res = res % 100000
                
print(res)
