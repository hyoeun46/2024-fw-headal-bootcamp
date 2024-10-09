def is_prime(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return None
    return True

M = int(input())
N = int(input())

primes = []

for i in range(M, N + 1):
    if is_prime(i):
        primes.append(i)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)