from main import factorial

def main():
    # Hardcoded test cases
    test_cases = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        10: 3628800,
    }

    print("Running factorial tests...")
    all_passed = True

    for n, expected in test_cases.items():
        try:
            result = factorial(n)
            if result == expected:
                print(f"factorial({n}) = {result} (PASS)")
            else:
                print(f"factorial({n}) = {result}, expected {expected} (FAIL)")
                all_passed = False
        except Exception as e:
            print(f"factorial({n}) raised {e} (FAIL)")
            all_passed = False

    if all_passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome test cases failed.")

if __name__ == "__main__":
    main()
