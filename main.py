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


# 22bcs068 (Reverse a String)

def reverse_string(s):
    return s[::-1]

# Example
text = "Hello World"
print("Original:", text)
print("Reversed:", reverse_string(text))

