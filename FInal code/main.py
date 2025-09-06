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

# 22bcs081 (Prime Number)
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

# # Example usage
# print(check_odd_even(10))  # Even
# print(check_odd_even(7))   # Odd


# 22BCS080 (Matrix Operations)
class Matrix:
    """
    Class to perform some Matrix Operations like:
    - Addition
    - Multiplication
    - Transpose
    - Determinant
    - Power
    using user inputs
    """

    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError(" Please make sure all rows have the same number of columns")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return "\n".join(str(row) for row in self.data)

    # ---------- Method to take user input ----------
    @classmethod
    def from_user_input(cls):
        """
        Function to take user inputs and create a Matrix
        """
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        print(f"Please enter the elements to be used in the matrix separated by spaces and press Enter when completed entering elements for a row...")

        data = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                raise ValueError("Number of elements in row must match the specified number of columns")
            data.append(row)

        return cls(data)

    # ---------- Function to find the Transpose of the matrix ----------
    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)])
    
    # ---------- Function to add two matrices ----------
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    # ---------- Function to multiply two matrices ----------
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix A's Dimensions must be compatible with Matrix B's Dimensions for multiplication")
        result = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    # ---------- Function to find the Determinant of the matrix ----------
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant requires a square matrix and square matrix was not provided")

        n = self.rows
        if n == 1:
            return self.data[0][0]
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0
        for c in range(n):
            minor = [row[:c] + row[c+1:] for row in self.data[1:]]
            det += ((-1) ** c) * self.data[0][c] * Matrix(minor).determinant()
        return det

    # ---------- Function to find the Power of the matrix ----------
    def power(self, k):
        if self.rows != self.cols:
            raise ValueError("Power requires a square matrix and square matrix was not provided")

        result = Matrix([[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)])
        base = self

        while k > 0:
            if k % 2 == 1:
                result = result.multiply(base)
            base = base.multiply(base)
            k //= 2
        return result

# 22bcs071 (factorial)
def factorial(n: int) -> int:
    """
    Compute factorial of a non-negative integer n.
    Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

