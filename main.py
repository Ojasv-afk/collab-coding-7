# main.py
"""
Starter File for Collab Coding
Group ID: 7
"""
# Collaborators add function here:
# 22bcs077(GCD)
def gcd(a, b):
    """
    GCD function
    Author: Ojasv-afk
    """
    while b:
        a, b = b, a % b
    return a
# 22bcs081(Factorial)
def factorial(n):
    """
    Factorial function
    Author
    :param n: non-negative integer
    :return: n!
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a non-negative integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result