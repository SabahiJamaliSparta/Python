# Object-oriented programming | Testing | File handling | CSV processin

## Contents

1. Classes and object-oriented programming
2. Unit testing, pytest and test-driven development
3. Text files and error handling
4. CSV reading, transformation and loading
5. Execution and documentation reference

## General terms

| Term | Definition |
| --- | --- |
| Function | Reusable code performing an operation. |
| Parameter | Input name in a function definition. |
| Argument | Value supplied when calling a function. |
| Return value | Result provided to calling code. |
| Method | A function associated with a class or object. |
| Module | An importable Python source file. |
| Import | Make definitions from another module available. |
| Working directory | Folder used to resolve ordinary relative paths. |
| __file__ | Module file path in the supplied scripts. |
| Path | A filesystem path object from pathlib. |
| with_name() | Construct a sibling path with another filename. |
| Pseudocode | Plain-language algorithm steps. |



# 1. Classes and OOP

OOP groups data and behaviour in objects. A class defines the structure; an instance is one object created from it.

| Term | Definition | Shopping-cart context |
| --- | --- | --- |
| Class | Blueprint for instances. | ShoppingCart |
| Object / instance | An individual created from a class. | One customer's cart |
| State | Current attribute values. | Customer and stored items |
| Attribute | Data attached to an object. | customer |
| Behaviour | Actions provided by methods. | Add an item or calculate a total |
| Method | Function belonging to a class or object. | add_item() |
| self | The current instance. | The cart being changed |
| __init__ | Initialises instance state. | Start with an empty cart |
| Supertype | More general type. | ShoppingCart |
| Subtype | More specific type. | MemberCart |
| Overriding | Replace inherited behaviour with a child method. | Member checkout calculation |

## Four principles

| Principle | Meaning | Why use it? |
| --- | --- | --- |
| Encapsulation | Group data and behaviour and control normal direct access to internal data. | Keep changes consistent. |
| Abstraction | Hide implementation details behind useful operations. | Make code easier to use. |
| Inheritance | Reuse or extend a base class. | Share behaviour across suitable related types. |
| Polymorphism | Use the same operation with different implementations. | Work with different object types through a shared interface. |

Python's __name convention triggers name mangling; it does not make data completely inaccessible. A single leading underscore marks an internal name by convention.

## Reference pseudocode

CREATE a cart for a customer
STORE its items as state
PROVIDE methods to add items and calculate totals
REUSE common behaviour for different cart types
SPECIALISE checkout behaviour where needed

The shopping-cart practice exercise is maintained separately from the reference documentation.



## Inheritance and attribute access

| Syntax | Meaning | Shopping-cart context |
| --- | --- | --- |
| class Child(Parent) | Declare inheritance. | MemberCart inherits ShoppingCart. |
| super().__init__(...) | Initialise state through the next class in the method-resolution order; the parent in these simple examples. | Initialise shared customer and item data. |
| @property | Read a method result as an attribute. | cart.item_count |
| @price.setter | Run a setter when a property is assigned. | Check a product price before changing it. |
| __price | Name-mangled internal attribute. | Keep the stored price behind a property. |

Getter: retrieve a value. Setter: manage assigning a value. A setter only performs validation or authentication if that code is actually implemented. A setter performs validation or authentication only when that behaviour is implemented.

# 2. Unit testing and pytest

A unit test checks a small part of behaviour against an expected result. Tests catch mistakes and help detect when later changes break existing cases.

The calculator does the work. The test files check its answers.

## Files and run order

| File | Purpose |
| --- | --- |
| calculator.py | Define add() and subtract(). |
| test_calculator.py | Five unittest checks. |
| test_calculator_pytest.py | Three parameter rows and two ordinary pytest tests. |
| convert.py | Celsius-to-Fahrenheit conversion. |
| test_convert.py | Two temperature conversion checks. |

Run commands from this folder:

```bash
python3 -m unittest test_calculator -v
python3 -m pytest test_calculator_pytest.py test_convert.py -v
```

If pytest is missing, install it in your selected interpreter:

```bash
python3 -m pip install pytest
```

Running pytest with no filename in this folder also collects the unittest tests: twelve checks altogether.

## How a check works

```python
actual_result = add(10, 6)
expected_result = 16
```

The unittest method compares them:

```python
self.assertEqual(actual_result, expected_result)
```

The equivalent pytest check is:

```python
assert add(10, 6) == 16
```

These snippets illustrate lines inside the supplied test files; imports and test structure are provided there.

## Parametrization

The decorator supplies rows of inputs and expected outputs to one test function:

| num1 | num2 | expected_result |
| --- | --- | --- |
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 1 | 10 | 11 |

The function runs once per row. This avoids repeating the same checking logic.

## Pseudocode

ARRANGE the input values
ACT by calling the function
ASSERT that actual and expected results match
REPEAT for each test case
REPORT passes, failures or errors

## Terms

| Term | Simple meaning |
| --- | --- |
| unittest | Built-in Python testing framework. |
| pytest | External testing framework. |
| TestCase | Base class providing unittest checks. |
| test_ prefix | Default prefix used to identify test functions or methods. |
| Assertion | Check that an expected condition holds. |
| assert | Python statement that raises AssertionError if false. |
| assertEqual(a, b) | Check equality. |
| assertNotEqual(a, b) | Check inequality. |
| assertTrue(value) | Check truthiness. |
| assertFalse(value) | Check falsiness. |
| assertIsNone(value) | Check the value is None. |
| assertRaises(ErrorType) | Check that an operation raises the specified exception. |
| Actual result | What the function returned. |
| Expected result | What it should return. |
| Decorator | Behaviour attached above a function using @. |
| parametrize | Repeat a test with different supplied arguments. |
| Test runner | Executes tests and reports results. |
| unittest.main() | Run tests in the current module. |
| -m | Run a module using the chosen Python interpreter. |
| OK / passed | All completed checks matched expectations. |
| Failure | An assertion was not satisfied. |
| Error | An unexpected exception prevented normal completion. |

Passing cases do not prove correctness for every input. A function that always returns 2 passes the 1 + 1 check but fails other sums. Assert statements are for checking assumptions and tests, not validating user input; Python optimisation can remove ordinary assertions.



## Temperature conversion and type hints

The converter uses Celsius × 9 / 5 + 32. Its tests check 0 → 32 and 100 → 212.

| Syntax | Meaning |
| --- | --- |
| celsius: float | A type hint describing the intended input. |
| -> float | A type hint describing the intended return type. |
| Triple-quoted text | A docstring describing the function. |

Type hints do not automatically enforce types at runtime.

## Test-driven development (TDD)

TDD is the practice of writing a test before implementing the required behaviour.

1. **Red:** observe a failing test for the missing behaviour.
2. **Green:** implement the required behaviour so the test passes.
3. **Refactor:** improve the code and rerun tests.

The counting practice exercise is incomplete: its function returns an integer, while its test indexes the result. The test therefore raises TypeError. Even after passing, that first check alone would not establish that the entire sequence is correct. The exercise is maintained separately from completed examples.

# 3. Text files and error handling

File handling reads or writes stored data. An exception interrupts normal execution; try/except handles selected errors.

## Files and order

| File | Purpose |
| --- | --- |
| orders.py | Define reading and appending functions. |
| file_handling.py | Call the functions using a practice output path. |
| order_example.txt | Example order text. |
| order_practice.txt | Generated when the demonstration runs. |

Run file_handling.py in PyCharm, or from this folder:

```bash
python3 file_handling.py
```

Each run appends beans once and prints the stored lines. Repeated runs therefore show additional beans lines.

## Main tools

| Tool | Meaning |
| --- | --- |
| open(path, mode) | Open a file and return a file object. |
| "r" | Read existing contents. |
| "w" | Write; creates a file or erases existing contents first. |
| "a" | Append; retain existing contents and add at the end. |
| "x" | Create exclusively; fail if a file already exists. |
| with | Manage the file and close it when the block exits. |
| readlines() | Read all remaining lines into a list. |
| write(text) | Write one string; no automatic newline. |
| rstrip("\n") | Remove trailing newline characters. |
| "\n" | Newline character. |
| encoding="utf-8" | Specify the text encoding. |
| try | Attempt an operation that might raise an exception. |
| except | Handle a matching exception. |
| as errmsg | Bind the exception to a name for displaying details. |
| FileNotFoundError | The requested file or part of its path cannot be found. |
| FileExistsError | An exclusive creation operation encounters an existing file. |
| raise | Raise an exception; a bare raise re-raises the current one. |
| finally | Run cleanup when leaving try, whether or not it succeeds. |

FileExistsError is not needed for ordinary read mode. Append mode creates a missing file, but cannot create missing parent folders.

## Reading pseudocode

TRY to open the file in read mode
READ all lines
FOR each line, remove its ending newline and PRINT
CLOSE automatically when leaving with
IF the file cannot be found, DISPLAY the error

## Writing pseudocode

TRY to open the file in append mode
WRITE one order item followed by a newline
CLOSE automatically when leaving with
IF the path cannot be found, DISPLAY the error

The writer accepts one string, such as beans. It does not take a list of orders in this version.

# 4. CSV reading, selecting and writing

CSV stores tabular rows as text with separators, commonly commas. Python's csv module reads rows and writes selected data.

## Dataset structure

user_details.csv is the original five-column input. new_user_details.csv is the corresponding three-column output.

| Index | Source column | Selection |
| --- | --- | --- |
| 0 | Title | Omitted |
| 1 | firstName | Retained |
| 2 | lastName | Retained |
| 3 | gender | Omitted |
| 4 | email | Retained |

The working scripts use this supplied input. 

## Execution order

Inspect rows with csv_file_handling.py. Select columns in csv_file_handling_transform.py. Write results through csv_file_handling_load.py. Start the process using csv_controller.py.

The controller creates practice_selected_users.csv beside itself. 
## Processing algorithm

OPEN the source CSV
READ each row
CHECK that the required positions exist
SELECT positions 1, 2 and 4
APPEND the selected row to the result list
RETURN the result list
OPEN the output only after selection succeeds
WRITE all result rows
REPORT success or the handled error

## Terms

| Term | Meaning |
| --- | --- |
| CSV | Comma-separated values; a text table format. |
| csv.reader() | Produce rows as lists of strings. |
| delimiter="," | Specify the column separator. |
| newline="" | Let the csv module handle newline conventions. |
| csv.writer() | Create a CSV writer. |
| writerow(row) | Write one row. |
| writerows(rows) | Write multiple rows. |
| append() | Add one item to a list. |
| user[1] | Select the second value in the current row. |
| Header | Row naming the columns. |
| Transform | Change the arrangement or content of data. |
| Load | Write processed data to a destination. |
| ETL | Extract, transform, load; this example reads, selects and writes. |
| ValueError | Here, signals that a row cannot satisfy the required shape. |

The CSV reader returns strings under the settings used here. Convert numeric fields explicitly if later calculations require numbers.

# 5. Execution and references

## Open and run the project

1. Extract Python_Study_Pack.zip.
2. Open the extracted Python_Study_Pack folder in PyCharm.
3. Select the Python interpreter.
4. Install pytest if needed using python3 -m pip install -r requirements.txt.
5. Follow each topic's execution instructions.

| Folder | Purpose |
| --- | --- |
| 01_oop | OOP concepts and terminology. |
| 02_unit_testing | Calculator, conversion and associated tests. |
| 03_files_and_error_handling | Text-file functions and their controller. |
| 04_csv_handling | CSV input, transformation and output. |
| practice | Shopping-cart and property examples; incomplete TDD exercise. |

| File format | Application |
| --- | --- |
| .pdf | Browser or PDF viewer. |
| .md | Markdown viewer or text editor. |
| .py | PyCharm or another code editor. |
| .csv | Text editor or spreadsheet application. |
| .zip | Extract before opening its contained files. |

## Official documentation

- Python: https://docs.python.org/3/
- Classes: https://docs.python.org/3/tutorial/classes.html
- Modules: https://docs.python.org/3/tutorial/modules.html
- unittest: https://docs.python.org/3/library/unittest.html
- File input/output: https://docs.python.org/3/tutorial/inputoutput.html
- Exceptions: https://docs.python.org/3/tutorial/errors.html
- CSV: https://docs.python.org/3/library/csv.html
- pathlib: https://docs.python.org/3/library/pathlib.html
- pytest: https://docs.pytest.org/en/stable/getting-started.html
- Parametrization: https://docs.pytest.org/en/stable/how-to/parametrize.html

Definitions are concise paraphrases. Python's documentation covers its language and standard library; pytest has its own official documentation.
