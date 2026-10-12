# 10. Control flow exercises
# Run this file with Python 3. No external packages required.

print("\nQ1a\n")
# Q1a — Print the first five list elements
# Count and print the first five elements
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
counter = 1

for number in x:
    if counter <= 5:
        print(number)
    counter += 1

print("\nQ1b\n")
# Q1b — Print all even elements
# Print elements divisible by two
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

for number in x:
    if number % 2 == 0:
        print(number)

print("\nQ1c\n")
# Q1c — Print even values among the first five elements
# Count elements and print even values within the first five
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
counter = 1

for number in x:
    if counter <= 5 and number % 2 == 0:
        print(number)
    counter += 1

print("\nQ2a\n")
# Q2a — Collect first-name initials
# Extract first-name initials into a list
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
initials = []

for name in names:
    initials.append(name[0])

print(initials)

print("\nQ2b\n")
# Q2b — Collect the space indexes
# Record the position of the first space in each name
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
space_indexes = []

for name in names:
    space_indexes.append(name.index(" "))

print(space_indexes)

print("\nQ2c\n")
# Q2c — Collect first-name and surname initials
# Combine each person's first and last initials
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
initials = []

for name in names:
    space_index = name.index(" ")
    initials.append(name[0] + name[space_index + 1])

print(initials)

print("\nQ3a\n")
# Q3a — Print inner lists without duplicates
# Select lists containing only unique values
list_of_lists = [
    [1, 5, 7, 3, 44, 4, 1],
    ["A", "B", "C"],
    ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
    ["one", "Two", "Three", "Four"]
]

for items in list_of_lists:
    if len(items) == len(set(items)):
        print(items)

print("\nQ4a\n")
# Q4a — Request an integer greater than 100
# Repeat input until the integer exceeds 100
while True:
    try:
        number = int(input("Enter a whole number greater than 100: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if number > 100:
        break
    print("The number must be greater than 100.")

print(number)

print("\nQ4b\n")
# Q4b — Classify the accepted number as prime or not prime
# Continue with the number accepted in Q4a
is_prime = True

# Stop searching when an additional divisor is found
for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print("prime")
else:
    print("not prime")

