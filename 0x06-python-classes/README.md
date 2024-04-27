# Python - Classes and Objects

In this repository, I explored the fundamentals of object-oriented programming (OOP) using Python. Throughout the project, I delved into concepts such as classes, objects, attributes, methods, properties, data abstraction, data encapsulation, and information hiding.

## Tasks :page_with_curl:

* **0. My First Square**
  * File: [0-square.py](./0-square.py)
  * Description: This is my initial implementation of the Python class `Square` that defines a square.

* **1. Square with Size**
  * File: [1-square.py](./1-square.py)
  * Description: I extended the `Square` class from [0-square.py](./0-square.py) with:
    * A private instance attribute `size`.
    * Instantiation that accepts `size` as a parameter.

* **2. Size Validation**
  * File: [2-square.py](./2-square.py)
  * Description: Building on [1-square.py](./1-square.py), I added:
    * Optional instantiation with `size`: `def __init__(self, size=0):`
    * Check for integer validity; raise a `TypeError` if not an integer.
    * Check for size validity; raise a `ValueError` if size is less than `0`.

* **3. Area of a Square**
  * File: [3-square.py](./3-square.py)
  * Description: Extending [2-square.py](./2-square.py), I incorporated:
    * A public instance attribute `def area(self):` to calculate and return the square's area.

* **4. Access and Update Private Attribute**
  * File: [4-square.py](./4-square.py)
  * Description: I improved [3-square.py](./3-square.py) with:
    * A property `def size(self):` to access the private instance attribute `self.size`.
    * A property setter `def size(self, value):` to update `self.size`.

* **5. Printing a Square**
  * File: [5-square.py](./5-square.py)
  * Description: Continuing from [4-square.py](./4-square.py), I added:
    * A public instance method `def my_print(self):` to print the square using `#`.
    * Special handling for an empty line when `size` is 0.

* **6. Coordinates of a Square**
  * File: [6-square.py](./6-square.py)
  * Description: Further building upon [5-square.py](./5-square.py), I introduced:
    * A private instance attribute `position`.
    * A property `def position(self):` to access `position`.
    * A property setter `def position(self, value):` to update `position`.
    * Instantiation that accepts optional `size` and `position`.

* **7. Singly Linked List**
  * File: [100-singly_linked_list.py](./100-singly_linked_list.py)
  * Description: I defined Python classes `Node` and `SinglyLinkedList` to create a singly-linked list. For `Node`:
    * Private instance attributes `data` and `next_node`.
    * Property methods for `data` and `next_node`.
    * Instantiation with `data` and `next_node`.

  * Description (Continued): For `SinglyLinkedList`:
    * Private instance attribute `head`.
    * Instantiation `def __init__(self):`
    * Public instance method `def sorted_insert(self, value):` to insert a `Node` while maintaining sorting order.

* **8. Print Square Instance**
  * File: [101-square.py](./101-square.py)
  * Description: I enhanced [6-square.py](./6-square.py) with a `__str__` method to enable printing of a `Square` instance similar to `my_print()`.

* **9. Compare 2 Squares**
  * File: [102-square.py](./102-square.py)
  * Description: Continuing from [101-square.py](./101-square.py), I implemented methods `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__` to facilitate logical comparisons between `Square` instances based on their areas.

* **10. ByteCode -> Python #5**
  * File: [103-magic_class.py](./103-magic_class.py)
  * Description: I created a Python function to exactly match a provided bytecode.

Please ensure that all content is written in the English language.
