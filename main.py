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

# ...existing code...
# 22bcs081 (Prime Number)
def is_prime(n):
    """
    Check if a number is prime
    Author: 22bcs081
=======
    return a
# 22bcs081(Prime)
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    Author: Snehith
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



# 22bcs068 (Even/odd number)

def check_odd_even(num: int) -> str:
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# Example usage
print(check_odd_even(10))  # Even
print(check_odd_even(7))   # Odd
