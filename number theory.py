import random

def gcd(a, b):
    """Finds the Greatest Common Divisor (GCD) using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Finds the Least Common Multiple (LCM) using the formula: LCM(a, b) = (a * b) / GCD(a, b)."""
    return (a * b) // gcd(a, b)

def is_coprime(a, b):
    """Checks if two numbers are coprime (GCD = 1)."""
    return gcd(a, b) == 1

def modular_exponentiation(base, exponent, modulus):
    """Computes (base^exponent) % modulus efficiently using Fast Exponentiation."""
    result = 1
    base = base % modulus  # Reduce base if greater than modulus

    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd, multiply base with result
            result = (result * base) % modulus
        base = (base * base) % modulus  # Square the base
        exponent //= 2  # Reduce exponent by half

    return result

def extended_gcd(a, b):
    """Returns GCD of a and b, along with x and y such that ax + by = GCD(a, b)."""
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def modular_inverse(a, m):
    """Finds the modular inverse of a under modulo m, if it exists."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse doesn't exist if GCD is not 1
    else:
        return x % m  # Ensure result is in the range [0, m-1]

def main():
    while True:
        print("\nChoose an operation:")
        print("1. GCD (Greatest Common Divisor)")
        print("2. LCM (Least Common Multiple)")
        print("3. Coprimality Check")
        print("4. Modular Exponentiation")
        print("5. Modular Inverse (Extended Euclidean Algorithm)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':  # GCD Calculation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = gcd(num1, num2)
            print(f"GCD of {num1} and {num2} is {result}")

        elif choice == '2':  # LCM Calculation
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = lcm(num1, num2)
            print(f"LCM of {num1} and {num2} is {result}")

        elif choice == '3':  # Coprimality Check
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = is_coprime(num1, num2)
            print(f"{num1} and {num2} are {'coprime' if result else 'not coprime'}.")

        elif choice == '4':  # Modular Exponentiation
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            modulus = int(input("Enter the modulus: "))
            result = modular_exponentiation(base, exponent, modulus)
            print(f"({base}^{exponent}) % {modulus} = {result}")

        elif choice == '5':  # Modular Inverse
            num = int(input("Enter the number: "))
            mod = int(input("Enter the modulus: "))
            result = modular_inverse(num, mod)
            if result is None:
                print(f"No modular inverse exists for {num} under modulo {mod}.")
            else:
                print(f"The modular inverse of {num} under modulo {mod} is {result}")

        elif choice == '6':  # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
