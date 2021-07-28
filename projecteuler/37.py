LIMIT = pow(10, 6) + 17

def generatePrime(n):
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, n):
        if isPrime[i]:
            for j in range(2, n // i):
                isPrime[i * j] = False
                
    return isPrime


def convertLeft(s):
    return s[1:]


def convertRight(s):
    return s[:-1]

n = int(input().strip())
isPrime = generatePrime(LIMIT)
res = 0
for i in range(10, n):
    if (isPrime[i]):
        t = convertRight(str(i))
        flag = True
        while len(t) > 0:
            if not isPrime[int(t)]:
                flag = False
                break
            t = convertRight(t)
        t = convertLeft(str(i))
        while len(t) > 0:
            if not isPrime[int(t)]:
                flag = False
                break
            t = convertLeft(t)
                
        if flag:
            res += i
            
print(res)
