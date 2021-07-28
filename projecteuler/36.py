n, k = input().strip().split(" ")
n, k = int(n), int(k)


def convert(n, k):
    convertString = "0123456789ABCDEF"
    if n < k:
        return convertString[n]
    else:
        return convert(n//k,k) + convertString[n%k]

res = 0
for i in range(n):
    if str(i) == str(i)[::-1]:
        s = convert(i, k)
        if s == s[::-1]:
            res += i

print(res)
