def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [num for num in range(2, n + 1) if is_prime[num]]

n = 40_000_000
primes = sieve_of_eratosthenes(n)
print(f"Found {len(primes)} primes up to {n:,}")
print(f"First 10: {primes[:10]}")
print(f"Last 10:  {primes[-10:]}")
