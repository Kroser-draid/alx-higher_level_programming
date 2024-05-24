# Python - Exceptions

In this project, I've focused on error and exception handling in Python using the `try` and `except` constructs.

## Function Prototypes :

Below are the function prototypes for the tasks completed in this project:

| File                             | Prototype                                               |
| -------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`           | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`        | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`  | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`       | `def safe_print_division(a, b):`                        |
| `4-list_division.py`             | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`           | `def raise_exception():`                                |
| `6-raise_exception_msg.py`       | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`  | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`           | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`       | `def magic_calculation(a, b);`                          |
| `103-python.c`                   | `void print_python_list(PyObject *p);`<br>`void print_python_bytes(PyObject *p);`<br>`void print_python_float(PyObject *p);` |

## Tasks :

* **0. Safe list printing**
  * [0-safe_print_list.py](./0-safe_print_list.py): Defines a Python function to print `x` elements from a list on the same line, followed by a newline.
  * Parameter `x` can exceed the length of `my_list`.
  * Returns the actual number of elements printed.
  * Achieved without using modules or `len()`.

* **1. Safe printing of an integers list**
  * [1-safe_print_integer.py](./1-safe_print_integer.py): Implements a Python function to print an integer using the `"{:d}".format()` format.
  * The parameter `value` can have any type.
  * Returns `True` if printing was successful (integer input), else `False`.
  * Accomplished without importing modules or using `type()`.

* **2. Print and count integers**
  * [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): Defines a Python function to print the first `x` integer elements of a list on the same line, followed by a newline.
  * Parameter `my_list` can include any type.
  * The parameter `x` determines how many elements to print, even beyond `my_list` length.
  * Returns the actual count of integers printed.
  * Without importing modules or using `len()`.

* **3. Integers division with debug**
  * [3-safe_print_division.py](./3-safe_print_division.py): Implements a Python function for dividing two integers and printing the result using `finally:`.
  * Assumes input arguments are integers.
  * Returns division result on success; otherwise, returns `None`.
  * Done without importing modules.

* **4. Divide a list**
  * [4-list_division.py](./4-list_division.py): Defines a Python function to element-wise divide two lists.
  * Returns a new list of length `list_length` with division results.
  * Both input lists, `my_list_1` and `my_list_2`, can contain any type.
  * Parameter `list_length` can exceed individual list lengths.
  * Handles various errors like non-numeric elements and division by zero.
  * Achieved without importing modules.

* **5. Raise exception**
  * [5-raise_exception.py](./5-raise_exception.py): Implements a Python function to raise a custom exception type.
  * Without importing modules.

* **6. Raise a message**
  * [6-raise_exception_msg.py](./6-raise_exception_msg.py): Defines a Python function to raise an exception with a custom message.
  * Without importing modules.

* **7. Safe integer print with error message**
  * [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): Implements a Python function to print an integer using `"{:d}".format()`, with type-checking.
  * The parameter `value` can have any type.
  * Returns `True` if printing was successful (integer input), otherwise prints an error to `stderr` and returns `False`.
  * Done without importing modules.

* **8. Safe function**
  * [101-safe_function.py](./101-safe_function.py): Implements a Python function to safely execute another function.
  * Assumes the parameter `fct` is always a pointer to a function.
  * Returns function result on success; otherwise, prints an error to `stderr` and returns `None`.

* **9. ByteCode -> Python #4**
  * [102-magic_calculation.py](./102-magic_calculation.py): Defines a Python function to match a specific provided bytecode.

* **10. CPython #2: PyFloatObject**
  * [103-python.c](./103-python.c): C functions that provide basic information about Python lists, bytes, and float objects.
