"""
Instructions:

Given a string of digits, calculate the largest product for a contiguous substring of digits of length n.
"""

def largest_product(series, size):
    if size > len(series) or not str(size).isdigit() or size < 0:
        raise ValueError("Invalid input!")
    largest_so_far = 0
    for i in range(len(series) - size + 1):
        list_of_nums = [int(j) for j in series[i:i+size]]
        result = 1
        for k in list_of_nums:
            result = result * k
        if result > largest_so_far:
            largest_so_far = result
    return largest_so_far
