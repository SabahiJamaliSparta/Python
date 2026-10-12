# Introduction to Python
### Foundations, control flow, functions and lambda exercises

Learning notes for **Sabahi Jamali — Sparta Global**.

This README brings together the Python concepts and exercises studied so far. Examples use simple Python 3 syntax, concise pseudocode comments and brief explanations. No external packages are required.

## Contents

- [1. What is Python?](#1-what-is-python)
- [2. Running Python](#2-running-python)
- [3. Syntax and variables](#3-syntax-and-variables)
- [4. Data types](#4-data-types)
- [5. Operators](#5-operators)
- [6. Strings, lists and built-in tools](#6-strings-lists-and-built-in-tools)
- [7. Control flow](#7-control-flow)
- [8. Functions](#8-functions)
- [9. Function exercises](#9-function-exercises)
- [10. Control flow exercises](#10-control-flow-exercises)
- [11. Lambda, recursion and map](#11-lambda-recursion-and-map)
- [12. Ten foundation practice questions](#12-ten-foundation-practice-questions)
- [13. Common errors and checks](#13-common-errors-and-checks)
- [14. Key terms](#14-key-terms)
- [15. Official references](#15-official-references)

## 1. What is Python?

Python is a high-level, general-purpose programming language used to develop software, automate tasks and analyse data. Its readable syntax allows instructions to be expressed without managing low-level hardware details.

In data science, Python supports:

- **Data preparation:** collecting, cleaning and transforming data.
- **Analysis:** exploring datasets, calculating statistics and identifying patterns.
- **Visualisation:** creating charts to communicate findings.
- **Machine learning:** building and evaluating predictive models.
- **Automation:** creating repeatable data pipelines and reports.

A **library** is a collection of reusable code. Examples used in data science include pandas for tabular data, NumPy for numerical arrays, Matplotlib for charts and scikit-learn for machine learning. These are external packages; the exercises here use built-in Python tools.

## 2. Running Python

| Environment | Purpose |
| --- | --- |
| PyCharm | An IDE for writing, running and debugging Python projects. |
| VS Code | An editor that supports Python development through extensions. |
| Jupyter Notebook / JupyterLab | Run code in cells alongside explanations and charts. |
| Google Colab | Work with Python notebooks in a browser. |
| Terminal / Command Prompt | Run scripts or start an interactive Python session. |
| IDLE | A basic Python editor and interactive shell. |

Python runs on Windows, macOS and Linux.

### Run an exercise in PyCharm

1. Open your Python project and select its Python interpreter.
2. Create a Python file, such as `control_flow.py`.
3. Copy the relevant code block into the file.
4. Right-click the file and select **Run**.
5. Check the output in the Run window. For `input()`, type your response there and press Enter.

An **interpreter** executes Python code. An **IDE** combines tools such as an editor, runner and debugger; it uses an interpreter to execute your program.

For a saved script, a terminal command is:

```bash
python3 control_flow.py
```

Depending on your installation, the command may be `python` instead of `python3`.

The README itself is documentation. Run its Python code blocks in `.py` files. Each exercise block below includes its dependencies and can run independently.

## 3. Syntax and variables

**Syntax** is the set of rules used to write valid code.

```python
# Assign values and display a greeting
name = "Sabahi"
age = 25

print("Hello, {name}!")
print(age)
```

**How it works:** `=` assigns a value to a variable. `print()` displays output. An f-string inserts values inside `{}`.

A **variable** is a name that refers to a value. Python determines the value's type at runtime; you do not have to declare it first.

### Main rules

| Rule | Example |
| --- | --- |
| Names are case-sensitive | `name` and `Name` are different names. |
| Use quotes for strings | `"Python"` or `'Python'`. |
| Use a colon before a code block | `if age >= 18:`. |
| Indentation groups instructions | Use four spaces consistently within a block. |
| Comments begin with `#` | `# Initialise result list`. |
| Use meaningful names | `total_sales` rather than `ts`. |
| Names cannot begin with a digit | `score_1` is valid; `1_score` is not. |
| Avoid reserved keywords as names | Do not name a variable `for` or `return`. |

```python
age = 25

# Display classification if condition is satisfied
if age >= 18:
    print("Adult")
```

## 4. Data types

A **data type** defines the kind of value held, how it is represented and which operations it supports. Types affect calculations, memory usage and data processing.

| Type | Definition | Example |
| --- | --- | --- |
| `str` | Text; an immutable sequence of characters. | `name = "Sabahi"` |
| `int` | An integer, including negative numbers and zero. | `count = 12` |
| `float` | A floating-point number, often used for decimals. | `price = 19.99` |
| `bool` | A logical value: `True` or `False`. | `is_valid = True` |
| `list` | An ordered, mutable collection. | `scores = [70, 85, 90]` |
| `tuple` | An ordered, immutable collection. | `point = (10, 20)` |
| `set` | A collection of unique, hashable values with no guaranteed iteration order. | `colours = {"red", "blue"}` |
| `dict` | A mutable mapping of unique keys to values. | `person = {"name": "Sabahi", "age": 25}` |
| `NoneType` | The type of `None`, representing the absence of a value. | `result = None` |

**Mutable** means an object can be changed after creation. **Immutable** means it cannot be changed in place. A variable can still be reassigned to a new object.

```python
# Inspect a type and convert numeric text
age = "25"
print(type(age))       # <class 'str'>

age = int(age)
print(type(age))       # <class 'int'>
print(age + 1)        # 26
```

**How it works:** `type()` identifies a value's type. `int()`, `float()` and `str()` convert suitable values between types.

Data example: `customer_id = "00123"` preserves leading zeros. Converting it to an integer produces `123`. Identifiers often belong in strings.

Floating-point values approximate many decimals, so small rounding differences can occur. Display rounding and exact decimal arithmetic are separate concerns.

## 5. Operators

An **operator** performs an operation on values.

### Arithmetic

| Operator | Meaning | Example result |
| --- | --- | --- |
| `+` | Addition | `3 + 2` → `5` |
| `-` | Subtraction | `3 - 2` → `1` |
| `*` | Multiplication | `3 * 2` → `6` |
| `/` | Division | `5 / 2` → `2.5` |
| `//` | Floor division; round quotient down | `5 // 2` → `2`; `-5 // 2` → `-3` |
| `%` | Modulo; division remainder | `5 % 2` → `1` |
| `**` | Exponentiation | `3 ** 2` → `9` |

### Assignment, comparison and logic

| Syntax | Meaning | Example |
| --- | --- | --- |
| `=` | Assign a value | `score = 70` |
| `+=` | Add to the current value and assign | `total += 5` |
| `==` / `!=` | Equal / not equal | `score == 70` |
| `>` / `<` | Greater / less than | `score > 65` |
| `>=` / `<=` | Greater / less than or equal | `score >= 65` |
| `and` | Both conditions must be true | `age >= 18 and has_ticket` |
| `or` | At least one condition must be true | `is_member or has_ticket` |
| `not` | Reverse a truth value | `not is_valid` |
| `in` / `not in` | Check membership | `2 in [1, 2, 3]` |

For the Boolean examples, define `age`, `has_ticket`, `is_member` and `is_valid` before using them.

## 6. Strings, lists and built-in tools

### Indexing and slicing

**Indexing** selects one item by position. Python starts counting at `0`.
**Slicing** selects a section; the start is included and the stop is excluded.

```python
numbers = [2, 5, 4, 87, 34, 2]

print(numbers[0])   # 2: first element
print(numbers[-1])  # 2: last element
print(numbers[:5]) # [2, 5, 4, 87, 34]

name = "Alan Turing"
print(name[0])          # A
print(name.index(" "))  # 4
print(name.lower())     # alan turing
```

### Common tools

| Tool | Purpose | Example |
| --- | --- | --- |
| `print()` | Display output. | `print("Hello")` |
| `input()` | Read user input as a string. | `name = input("Name: ")` |
| `type()` | Return a value's type. | `type(25)` |
| `int()` / `float()` / `str()` | Convert suitable values. | `int("25")` |
| `len()` | Count items or characters. | `len([2, 4])` → `2` |
| `range()` | Represent an integer sequence with an excluded stop. | `list(range(1, 5))` → `[1, 2, 3, 4]` |
| `abs()` | Return absolute value. | `abs(-12)` → `12` |
| `set()` | Collect unique values. | `set([1, 1, 2])` |
| `list()` | Collect iterable items into a list. | `list(range(3))` → `[0, 1, 2]` |
| `sum()` | Add numeric items. | `sum([1, 2, 3])` → `6` |
| `.append()` | Add one item to a list in place. | `numbers.append(10)` |
| `.index()` | Find the first matching position. | `"bob".index("o")` → `1` |
| `.lower()` | Return a lowercase string. | `"BOB".lower()` → `"bob"` |

A **method** is called through an object, such as `numbers.append(10)`. A built-in function is called directly, such as `len(numbers)`.

## 7. Control flow

**Control flow** determines which instructions run, in what order and how often.

### Conditions: if, elif and else

```python
number = -3

# Classify number by sign
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**How it works:** Python runs the first branch whose condition is true. `else` handles the remaining case. Output: `Negative`.

### For loop

```python
# Display integers from one to five
for number in range(1, 6):
    print(number)
```

A `for` loop processes each item in an iterable. An **iterable** supplies items one at a time, such as a list, string or range.

### While loop

```python
number = 1

# Repeat while the number does not exceed five
while number <= 5:
    print(number)
    number += 1
```

A `while` loop repeats while its condition is true. Updating `number` allows this loop to stop.

- **break:** exit the nearest enclosing loop.
- **continue:** skip the rest of the current iteration and begin the next.
- **Iteration:** one pass through a loop.

### Handling invalid input

```python
# Attempt integer conversion and handle invalid text
try:
    number = int(input("Enter a whole number: "))
    print(number)
except ValueError:
    print("Please enter a whole number.")
```

`try` contains an operation that might fail; `except` handles a matching exception.

## 8. Functions

A **function** is a reusable block of code that performs a task. It can take inputs and return a result.

```python
# Return the sum of two inputs
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)  # 7
```

| Term | Meaning | Example |
| --- | --- | --- |
| Definition | Create the function. | `def add_numbers(a, b):` |
| Parameter | An input name in the definition. | `a`, `b` |
| Argument | A value supplied when calling. | `3`, `4` |
| Call | Execute the function with supplied arguments. | `add_numbers(3, 4)` |
| Return | End the call and send a value back. | `return a + b` |
| Local variable | A name assigned within a function. | `result` inside a function body |

**Defining a function does not execute its body.** Calling it does.

**return versus print:** `return` supplies a result for other code to use; `print()` displays output. A function without an explicit return value returns `None`.

## 9. Function exercises

### Q1a — Return the positive divisors of an integer

```python
# Collect the positive divisors of an integer
def divisors(n):
    factors = []

    # Test each positive candidate
    for number in range(1, abs(n) + 1):
        if n % number == 0:
            factors.append(number)

    return factors

print(divisors(12))
```

**Output:** `[1, 2, 3, 4, 6, 12]`.

**How it works:** A zero remainder identifies a divisor. `+ 1` includes the upper candidate; `abs()` supports negative integers by returning their positive divisors.

**Scope:** For nonzero integers. For zero this implementation returns `[]`; zero has infinitely many nonzero integer divisors, so this is not a complete divisor list.

### Q1b — Check whether either integer is a factor of the other

```python
# Check divisibility in both directions
def is_factor(a, b):
    if a != 0 and b % a == 0:
        return True

    if b != 0 and a % b == 0:
        return True

    return False

print(is_factor(3, 12))  # True
print(is_factor(5, 12))  # False
```

**How it works:** Tests whether either number divides the other exactly. `and` skips the remainder calculation when the divisor is zero.

**Optional bonus — reuse Q1a for positive integer inputs:**

```python
def divisors(n):
    factors = []
    for number in range(1, n + 1):
        if n % number == 0:
            factors.append(number)
    return factors

def is_factor(a, b):
    # Check membership in either divisor list
    return a in divisors(b) or b in divisors(a)

print(is_factor(3, 12))  # True
```

**How it works:** Calls the previous function and checks whether one number appears in the other's divisors. This bonus version assumes both inputs are positive integers.

### Q2a — Return a letter's alphabet position

```python
# Return the zero-based position of a letter or space
def letter_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return alphabet.index(letter.lower())

print(letter_position("b"))  # 1
print(letter_position("O"))  # 14
```

**How it works:** Converts to lowercase and finds the character's position. These exercises use `a = 0`, matching the coach's example; a space is `26`.

### Q2b — Create a name ID from letter positions

```python
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
```

**How it works:** Joins `"1"`, `"14"` and `"1"` to produce the string `"1141"`. It concatenates positions rather than adding them.

### Q2c — Subtract the sum of ID digits from the numeric ID

```python
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
```

**How it works:** `1 + 1 + 4 + 1 = 7`, so `1141 - 7 = 1134`.

**Scope of Q2:** Use a nonempty name containing English letters and spaces. Other characters cause `index()` to raise `ValueError`. This ID scheme can produce collisions and the “password” is an exercise calculation, not a secure password generator.

### Q3a — Check whether an integer is prime

```python
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
```

**How it works:** A prime is greater than one and has no positive divisors other than one and itself. For `2`, the range is empty, so the function correctly returns `True`. This simple approach suits small practice inputs.

### Q3b — Handle invalid user text

```python
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
```

**How it works:** Converts text into an integer. Text such as `"hello"` or `"3.5"` produces a validation message instead of a crash.

**Scope:** This wrapper is designed for text from `input()`. Passing a float directly to `int()` truncates it rather than rejecting it.

## 10. Control flow exercises

### Q1a — Print the first five list elements

```python
# Count and print the first five elements
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
counter = 1

for number in x:
    if counter <= 5:
        print(number)
    counter += 1
```

**Output:** `2, 5, 4, 87, 34`, each on a separate line.

**How it works:** The counter starts at one and increases for each element. The condition prints only the first five values. Keep `print(number)` inside the `if` block.

### Q1b — Print all even elements

```python
# Print elements divisible by two
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

for number in x:
    if number % 2 == 0:
        print(number)
```

**Output:** `2, 4, 34, 2`, each on a separate line.

**How it works:** The condition checks each element's value, rather than its position.

### Q1c — Print even values among the first five elements

```python
# Count elements and print even values within the first five
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
counter = 1

for number in x:
    if counter <= 5 and number % 2 == 0:
        print(number)
    counter += 1
```

**Output:** `2, 4, 34`, each on a separate line.

**How it works:** The counter checks position and the modulo condition checks value. Increment the counter for every element, including odd values.

### Q2a — Collect first-name initials

```python
# Extract first-name initials into a list
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
initials = []

for name in names:
    initials.append(name[0])

print(initials)
```

**Output:** `['A', 'L', 'K', 'A', 'T']`.

**How it works:** Index zero selects the first character of each name.

### Q2b — Collect the space indexes

```python
# Record the position of the first space in each name
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
space_indexes = []

for name in names:
    space_indexes.append(name.index(" "))

print(space_indexes)
```

**Output:** `[4, 8, 9, 5, 7]`.

**How it works:** `index(" ")` finds the separator's zero-based position.

### Q2c — Collect first-name and surname initials

```python
# Combine each person's first and last initials
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]
initials = []

for name in names:
    space_index = name.index(" ")
    initials.append(name[0] + name[space_index + 1])

print(initials)
```

**Output:** `['AT', 'LF', 'KJ', 'AE', 'TT']`.

**How it works:** Combines the first character with the character after the first space. These name exercises assume the supplied nonempty two-part names with one space.

### Q3a — Print inner lists without duplicates

```python
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
```

**Output:**

```text
['A', 'B', 'C']
['one', 'Two', 'Three', 'Four']
```

**How it works:** A set removes duplicate values. Matching lengths show that none were removed. The original list is printed, preserving its order. This works for the hashable numbers and strings supplied here.

### Q4a — Request an integer greater than 100

```python
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
```

**How it works:** Invalid text restarts the loop. Integers at or below 100 are rejected. An accepted number exits the loop and is printed.

### Q4b — Classify the accepted number as prime or not prime

```python
# Validate input and classify the accepted integer
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
```

**How it works:** After input validation, the loop searches for an extra divisor. Finding one changes the flag to `False`; otherwise it stays `True`.

**Examples:** `101` prints `101` and `prime`; `102` prints `102` and `not prime`.

## 11. Lambda, recursion and map

A **lambda** creates a function from a single expression and returns that expression's result automatically.

```text
lambda parameters: expression
```

Before the colon are the inputs; after it is the calculation. A lambda is initially unnamed, but can be assigned to a variable.

Use lambdas for short operations, particularly when passing a function to another function. Prefer `def` for named reusable functions or multi-step logic. Assigning lambdas below demonstrates the exercise conversion.

### Q1a — Rewrite four functions as lambdas

```python
# Define single-expression calculations
square = lambda n: n * n
percentage = lambda n: n / 100
multiplier = lambda n, m: n * m
addition = lambda a, b, c: a + b + c

print(square(5))         # 25
print(percentage(50))    # 0.5
print(multiplier(3, 4))  # 12
print(addition(1, 2, 3)) # 6
```

| Function | Plain-language meaning |
| --- | --- |
| `square(5)` | Multiply five by itself. |
| `percentage(50)` | Divide fifty by 100 to get its decimal percentage form. |
| `multiplier(3, 4)` | Multiply the two inputs. |
| `addition(1, 2, 3)` | Add the three inputs. |

**How it works:** Each lambda returns its calculation without a `return` statement. It performs the same operation as the original `def` function.

Equivalent ordinary function:

```python
def square(n):
    return n * n

print(square(5))  # 25
```

**Why call it?** Defining the function records the operation. `square(5)` executes it with five as the input.

### Q1b — Explain the factorial lambda

```python
# Multiply down to one using recursive calls
factorial = lambda a: a * factorial(a - 1) if a > 1 else 1

print(factorial(4))  # 24
print(factorial(0))  # 1
```

**Factorial** means multiplying an integer by all the positive integers below it: `4! = 4 × 3 × 2 × 1 = 24`. By definition, `0! = 1`.

**How it works:**

1. If `a > 1`, request the factorial of the next smaller number.
2. Multiply that returned result by `a`.
3. At `a = 1`, return one without calling again.

For four, the calls request:

| Call | Result needed |
| --- | --- |
| `factorial(4)` | `4 * factorial(3)` |
| `factorial(3)` | `3 * factorial(2)` |
| `factorial(2)` | `2 * factorial(1)` |
| `factorial(1)` | `1`, the stopping result |

The results then return: `1 → 2 → 6 → 24`.

**Recursion** is a function calling itself. A **base case** is the stopping condition. The expression `result_if_true if condition else result_if_false` chooses between two values.

**Scope:** This teaching example assumes a small non-negative integer. It does not reject negative or non-integer inputs, and deep recursion can exceed Python's recursion limit.

### Q1c — Square a list using map and lambda

```python
# Apply squaring to each number and collect the results
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

squared_numbers = list(map(lambda n: n * n, list_of_numbers))

print(squared_numbers)
```

**Output:**

```text
[529, 119025, 2025, 5776, 7569, 16, 4, 0]
```

**How it works:**

- `lambda n: n * n` specifies the operation for one number.
- `map()` returns an iterator that applies the function to the supplied items as results are requested.
- `list()` consumes that iterator and stores the results in a list.

For example, 23 becomes `23 × 23 = 529`. The order of the input is preserved.

### Related terms: filter and sorted

These are optional examples extending the lambda concept.

```python
numbers = [5, 2, 8, 3]

# Keep values that satisfy the condition
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers)  # [2, 8]

names = ["Alan", "Leonardo", "Annie"]

# Order values by their character count
ordered_names = sorted(names, key=lambda name: len(name))
print(ordered_names)  # ['Alan', 'Annie', 'Leonardo']
```

**How it works:** `map()` transforms values; `filter()` selects values; `sorted()` returns a new sorted list. A `key` function determines the value used to compare items.

## 12. Ten foundation practice questions

1. Create variables for your name, age and favourite subject; print each.
2. Create a string, integer, float and Boolean; display each type with `type()`.
3. Create two numbers; print their sum, difference, product and division result.
4. Ask for a name and print a greeting.
5. Ask for an age and print the age next year.
6. Ask for an integer and classify it as positive, negative or zero.
7. Create a five-number list; print its first item, last item and length.
8. Use a `for` loop to print one through ten.
9. Use a `while` loop to print one through five.
10. Define a function that returns the sum of two numbers; call it and print the result.

## 13. Common errors and checks

| Error or issue | Meaning / correction |
| --- | --- |
| `SyntaxError` | Invalid syntax; check colons, quotes and brackets. |
| `IndentationError` | Incorrect indentation; align each block consistently. |
| `NameError` | A name has not been defined; check spelling and definition order. |
| `TypeError` | An operation receives an unsuitable type; check inputs. |
| `ValueError` | A suitable type contains an invalid value, such as `int("hello")`. |
| `IndexError` | A sequence position does not exist. |
| `ZeroDivisionError` | Division or modulo uses zero as the divisor. |
| `RecursionError` | Recursion exceeds the allowed depth. |
| Infinite loop | The stopping condition is never reached. |
| `=` instead of `==` | Assignment and equality comparison have different purposes. |
| `print()` instead of `return` | Displaying a result does not return it from a function. |

### Checking each exercise

- Run one exercise at a time and compare actual output with the documented example.
- Try a second valid input to check the logic.
- Try relevant boundaries: one and two for primality; 100 and 101 for the input threshold.
- Enter invalid text where validation is included.
- Read the final line of an error message and inspect the referenced code line.

Examples in this README are study solutions. Input assumptions are stated where validation is intentionally limited.

## 14. Key terms

| Term | Definition | Example |
| --- | --- | --- |
| Program / script | A set of instructions; a script is commonly saved as a code file. | `exercise.py` |
| Syntax | Rules for writing valid code. | A colon after `if`. |
| Variable | A name referring to a value. | `count = 5` |
| Data type | A value category that determines supported operations. | `int`, `str` |
| Expression | Code evaluated to a value. | `n * n` |
| Statement | An instruction executed by Python. | `return result` |
| Condition | An expression tested for truth. | `number > 100` |
| Boolean | A true or false value. | `True` |
| Sequence | An ordered collection accessible by position. | A list or string. |
| Iterable | An object that can supply items for iteration. | `range(5)` |
| Iterator | An object that supplies successive items and tracks progress. | The result of `map()`. |
| Element | One item in a collection. | `4` in `[2, 4, 6]`. |
| Index | A position in a sequence. | `names[0]` |
| Slice | A selected section of a sequence. | `x[:5]` |
| Concatenation | Joining sequences such as strings. | `"A" + "T"` |
| Control flow | The order and conditions of execution. | `if`, `for`, `while` |
| Iteration | One pass through a loop. | Processing one name. |
| Function | A reusable callable block of code. | `def square(n): ...` |
| Parameter | An input name in a function definition. | `n` |
| Argument | A value passed in a function call. | `5` in `square(5)`. |
| Return value | A result sent back by a call. | `25` |
| Method | A function accessed through an object or type. | `name.lower()` |
| Lambda | A function created with a single-expression syntax. | `lambda n: n * n` |
| Recursion | A function calling itself. | `factorial(a - 1)` |
| Base case | The condition ending recursive calls. | Return one at `a <= 1`. |
| Exception | An event interrupting normal execution, often signalling an error. | `ValueError` |
| Validation | Checking input against requirements. | Reject a number at or below 100. |
| Prime number | An integer greater than one with exactly two positive divisors. | `7` |
| Divisor / factor | A nonzero integer that divides another with no remainder. | `3` divides `12`. |
| Factorial | Product of positive integers up to a non-negative integer; `0! = 1`. | `4! = 24` |
| Pseudocode | A plain-language description of algorithm steps. | “Append each initial.” |
| Module | A unit of Python code that can be imported. | `import math` |
| Library | Reusable modules or packages providing related functionality. | Python's standard library. |

## 15. Official references

These notes paraphrase Python concepts and use original exercise examples. Refer to the official documentation for full details:

- [Python 3 documentation](https://docs.python.org/3/)
- [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [Numbers, strings and lists](https://docs.python.org/3/tutorial/introduction.html)
- [Control flow, function definitions and lambda expressions](https://docs.python.org/3/tutorial/controlflow.html)
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Built-in functions: input, range, map, filter and more](https://docs.python.org/3/library/functions.html)
- [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

The unversioned documentation links may change as Python releases advance. The examples here use established Python 3 features.

