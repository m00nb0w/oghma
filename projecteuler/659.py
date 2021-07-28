import math

MAX_VAL = pow(10, 6)

def generatePrime(n):
    isPrime = [True] * (n + 5)
    isPrime[0] = False
    isPrime[1] = False 
    primes = []
    for i in range(2, n):
        if isPrime[i]:
            primes.append(i)
            for j in range(2, n // i + 1):
                isPrime[i * j] = False
    return primes


if __name__ == "__main__":
    primes = generatePrime(MAX_VAL)
    for k in range(1, 100):
        maxP = 0 
        index = 0
        for n in range(1, 1000):
            x = n * n + k * k 
            y = (n + 1) * (n + 1) + k * k
            for p in primes:
                if (x % p == 0) and (y % p == 0): 
                    if p > maxP:
                        index = n
                        maxP = p
        print("For %d: max prime = %d at index %d" % (k, maxP, index))

