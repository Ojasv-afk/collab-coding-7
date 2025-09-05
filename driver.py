from main import *

def print_menu():
    print("\nMathematical Functions Menu:")
    print("1. Calculate GCD")
    print("2. Check Prime Number")
    print("3. Exit")
    print("\nEnter your choice (1-3): ")

def get_input():
    while True:
        try:
            choice = int(input())
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")

def handle_gcd():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = gcd(num1, num2)
        print(f"\nGCD of {num1} and {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")

def handle_prime():
    try:
        num = int(input("Enter a number to check: "))
        result = is_prime(num)
        print(f"\n{num} is {'prime' if result else 'not prime'}")
    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print_menu()
        choice = get_input()
        
        if choice == 1:
            handle_gcd()
        elif choice == 2:
            handle_prime()
        elif choice == 3:
            print("\nThank you for using the calculator!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("Welcome to Mathematical Functions Calculator!")
    main()
