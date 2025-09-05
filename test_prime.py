from main import is_prime

def main():
    # Small primes
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

    # Small non-primes
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

    # Larger primes
    assert is_prime(29) == True
    assert is_prime(97) == True
    assert is_prime(101) == True

    # Larger non-primes
    assert is_prime(100) == False
    assert is_prime(121) == False   # 11 * 11

    print("All prime tests passed!")

if __name__ == "__main__":
    main()
