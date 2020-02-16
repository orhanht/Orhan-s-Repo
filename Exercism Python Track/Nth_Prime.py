"""
Instructions:

Given a number n, determine what the nth prime is.
"""

def prime(number):
    if number == 0:
        raise ValueError("Invalid input!")
    prime_numbers = [2]
    count = 2
    while number > len(prime_numbers):
        is_prime = not (True in [count % i == 0 for i in prime_numbers])
        if is_prime:
            prime_numbers.append(count)
        count += 1
    return prime_numbers[-1]
