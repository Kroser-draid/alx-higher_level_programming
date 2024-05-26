# Python Test-Driven Development

This repository showcases the practice of test-driven development using `docstring` and `unittest` in Python.

## Tests

* **Test Files**:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function prototypes

Function prototypes for the implemented functions:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

## Tasks

1. **Integers Addition**
   * [0-add_integer.py](./0-add_integer.py): Function to add two integers.
   * Handles type errors and casting of floats.
   
2. **Divide a Matrix**
   * [2-matrix_divided.py](./2-matrix_divided.py): Divides matrix elements by a divisor.
   * Handles various error cases, including matrix format and division by zero.
   
3. **Say My Name**
   * [3-say_my_name.py](./3-say_my_name.py): Prints a formatted name.
   * Handles type errors for input names.
   
4. **Print Square**
   * [4-print_square.py](./4-print_square.py): Prints a square using `#`.
   * Validates size input and handles errors.
   
5. **Text Indentation**
   * [5-text_indentation.py](./5-text_indentation.py): Prints text with indentation.
   * Ensures proper formatting and handles type errors.
   
6. **Max Integer - Unittest**
   * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Unit tests for `max_integer` function.

7. **Matrix Multiplication**
   * [100-matrix_mul.py](./100-matrix_mul.py): Multiplies two matrices.
   * Covers multiple error scenarios and validations.
   
8. **Lazy Matrix Multiplication**
   * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Matrix multiplication using `NumPy`.
   * Similar to [100-matrix_mul.py](./100-matrix_mul.py).

9. **CPython #3: Python Strings**
   * [102-python.c](./102-python.c): C function printing basic info about Python string objects.
