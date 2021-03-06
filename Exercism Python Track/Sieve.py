"""
Instructions:

Use the Sieve of Eratosthenes to find all the primes from 2 up to a given number. The Sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e. not prime) the multiples of each prime, starting with the multiples of 2.
It does not use any division or remainder operation.
"""

def primes(limit):
    composite_nums = []
    prime_nums = []
    for i in range(2, limit + 1):
        if i not in composite_nums:
            prime_nums.append(i)
            for j in range(2, limit):
                if i * j <= limit:
                    composite_nums.append(i * j)
    return prime_nums
