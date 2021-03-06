"""
Instructions:

Detect palindrome products in a given range.
A palindromic number is a number that remains the same when its digits are reversed. 
For example, 121 is a palindromic number but 112 is not.
Given a range of numbers, find the largest and smallest palindromes which are products of numbers within that range.
Your solution should return the largest and smallest palindromes, along with the factors of each within the range.
If the largest or smallest palindrome has more than one pair of factors within the range, then return all the pairs.
"""

def products_of_factors(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Faulty input!")
    list_of_products = []
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            list_of_products.append(i * j)
    return list(set(list_of_products))


def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    return False


def factors_in_range(number, min_factor, max_factor):
    return [[i, number // i] for i in range(min_factor, max_factor + 1) if
            number % i == 0 and i <= number // i <= max_factor]


def largest(min_factor, max_factor):
    if len([i for i in products_of_factors(min_factor, max_factor) if is_palindrome(i)]) == 0:
        return None, []
    max_palindrome = max([i for i in products_of_factors(min_factor, max_factor) if is_palindrome(i)])
    return max_palindrome, factors_in_range(max_palindrome, min_factor, max_factor)


def smallest(min_factor, max_factor):
    if len([i for i in products_of_factors(min_factor, max_factor) if is_palindrome(i)]) == 0:
        return None, []
    min_palindrome = min([i for i in products_of_factors(min_factor, max_factor) if is_palindrome(i)])
    return min_palindrome, factors_in_range(min_palindrome, min_factor, max_factor)
