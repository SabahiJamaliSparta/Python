# 9. Function exercises
# Run this file with Python 3. No external packages required.

print("\nQ1a\n")
# Q1a — Return the positive divisors of an integer
# Collect the positive divisors of an integer
def divisors(n):
    factors = []

    # Test each positive candidate
    for number in range(1, abs(n) + 1):
        if n % number == 0:
            factors.append(number)

    return factors

print(divisors(12))

print("\nQ1b\n")
# Q1b — Check whether either integer is a factor of the other
# Check divisibility in both directions
def is_factor(a, b):
    if a != 0 and b % a == 0:
        return True

    if b != 0 and a % b == 0:
        return True

    return False

print(is_factor(3, 12))  # True
print(is_factor(5, 12))  # False

print("\nQ2a\n")
# Q2a — Return a letter's alphabet position
# Return the zero-based position of a letter or space
def letter_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet.index(letter.lower())

print(letter_position("b"))  # 1
print(letter_position("O"))  # 14

print("\nQ2b\n")
# Q2b — Create a name ID from letter positions
def letter_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet.index(letter.lower())

# Concatenate letter positions to form an ID
def name_id(name):
    id_number = ""
    for letter in name:
        id_number += str(letter_position(letter))
    return id_number

print(name_id("bob"))  # 1141

print("\nQ2c\n")
# Q2c — Subtract the sum of ID digits from the numeric ID
def letter_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet.index(letter.lower())

def name_id(name):
    id_number = ""
    for letter in name:
        id_number += str(letter_position(letter))
    return id_number

# Generate ID and subtract its digit total
def create_password(name):
    id_number = name_id(name)
    digit_total = 0
    for digit in id_number:
        digit_total += int(digit)
    return int(id_number) - digit_total

print(create_password("bob"))  # 1134

print("\nQ3a\n")
# Q3a — Check whether an integer is prime
# Determine whether the integer has exactly two positive divisors
def is_prime(n):
    if n < 2:
        return False

    # Search for a divisor other than one and n
    for number in range(2, n):
        if n % number == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(12))  # False
print(is_prime(1))   # False

print("\nQ3b\n")
# Q3b — Handle invalid user text
def is_prime(n):
    if n < 2:
        return False
    for number in range(2, n):
        if n % number == 0:
            return False
    return True

# Convert text input before checking primality
def check_prime(value):
    try:
        number = int(value)
    except (ValueError, TypeError):
        return "Please enter a whole number."
    return is_prime(number)

user_number = input("Enter a whole number: ")
print(check_prime(user_number))

