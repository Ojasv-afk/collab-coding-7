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