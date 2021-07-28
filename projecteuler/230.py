import sys

a = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
b = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

def f(i, n, d): 
    if i == 0:
        return a[n - 1]
    if i == 1:
        return b[n - 1]
    if n > d[i - 2]:
        return f(i - 1, n - d[i - 2], d)
    else:
        return f(i - 2, n, d)
    

q = 18
res = 0
for i in range(q):
    na = len(a)
    nb = len(b)
    n = (127 + 19 * i) * pow(7, i)

    if (na >= n):
        res += pow(10, i) * int(a[n - 1])
    elif (na + nb >= n):
        res += pow(10, i) * int(b[n - na - 1])
    else:
        d = [na, nb]
        t = 1
        # print(pow(2, 100))
        while d[-1] < n:
            d.append(d[-1] + d[-2])
            t += 1
        res += pow(10, i) * int(f(t, n, d))

print("The answer is %d" % res)
