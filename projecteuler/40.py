tests = int(input().strip())


power = [pow(10, i) for i in range(20)]

for _ in range(tests):
    a = [int(x) for x in input().strip().split(" ")]
    a.sort()
    
    t = 0
    j = 0
    i = 1
    res = 1
    while i < 20:
        if t + 9 * power[i - 1] * i < a[j]: 
            t += 9 * power[i - 1] * i
            i += 1
        else:
            n = a[j] - t - 1
            x = (n // i) + power[i - 1]
            res *= int(str(x)[n % i])
            j += 1
            if j == 7:
                break
    print(res)
