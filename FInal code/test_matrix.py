from main import Matrix

def main():
    '''
    Script to test the matrix class created in main.py with HARD-CODED test cases.
    - No user input
    - Matrices are pre-defined for testing
    - Menu works the same way
    '''
    print("=== Matrix Operations (Hardcoded Tests) ===")

    # Hardcoded Matrix A
    A = Matrix([[1, 2], [3, 4]])
    print("Matrix A:")
    print(A)

    while True:  
        print("\n" + "="*40)
        print("\nChoose operation:")
        print("1. Transpose")
        print("2. Add another matrix")
        print("3. Multiply by another matrix")
        print("4. Determinant")
        print("5. Power of matrix A w.r.t value k")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            print("\nTranspose of A:")
            print(A.transpose())

        elif choice == 2:
            # Hardcoded Matrix B for Addition
            B = Matrix([[5, 6], [7, 8]])
            print("\nMatrix B:")
            print(B)
            print("\nAddition result of A + B:")
            print(A.add(B))

        elif choice == 3:
            # Hardcoded Matrix B for Multiplication
            B = Matrix([[1, 0], [0, 1]])  # identity
            print("\nMatrix B:")
            print(B)
            print("\nMultiplication result of A * B:")
            print(A.multiply(B))

        elif choice == 4:
            if A.rows != A.cols:
                print("Determinant can only be calculated for square matrices")
            else:
                print("\nDeterminant of A is:", A.determinant())

        elif choice == 5:
            if A.rows != A.cols:
                print("Power can only be calculated for square matrices")
            else:
                k = 2  # Hardcoded power
                print("value of k is set to 2 for testing")
                print(f"\nPower of matrix A with respect to {k} is:")
                print(A.power(k))

        elif choice == 6:
            print("Exiting program!")
            break

        else:
            print("Please enter a valid choice (1-6)")

        # Always keep same Matrix A (skip asking user)
        print("\nKeeping the same Matrix A for all tests...")

if __name__ == "__main__":
    main()
