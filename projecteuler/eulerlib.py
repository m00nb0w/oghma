import math, sys

# Return a list 
# If i < n and isPrime[i] == True then i is prime and vice versa
def list_primality(n):
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, sqrt(n) + 1):
        if isPrime[i]:
            for j in range(2, n // i + 1):
                isPrime[i * j] = False
    return isPrime


# Return a list of primes less than N
def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

