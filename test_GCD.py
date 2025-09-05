from main import gcd

def main():
    assert gcd(10, 15) == 5
    assert gcd(7, 3) == 1

    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0 

    assert gcd(270, 192) == 6
    assert gcd(123456, 7890) == 6

    print("All tests passed!")

if __name__ == "__main__":
    main()