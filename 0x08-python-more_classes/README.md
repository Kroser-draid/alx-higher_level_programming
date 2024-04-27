# Python - More Classes and Objects - README

In this project, we explore object-oriented programming in Python, focusing on classes and objects. We cover key concepts like class methods, static methods, class vs. instance attributes, and the use of special methods like `__str__` and `__repr__`.

## Table of Contents

1. **Simple Rectangle**
   - [0-rectangle.py](./0-rectangle.py)
   - Defines an empty Python class representing a rectangle.

2. **Real Definition of a Rectangle**
   - [1-rectangle.py](./1-rectangle.py)
   - Extends the rectangle class with width and height attributes.
   - Implements getter and setter methods for width and height.
   - Handles data validation for integer values and non-negativity.

3. **Area and Perimeter**
   - [2-rectangle.py](./2-rectangle.py)
   - Adds methods to calculate the area and perimeter of the rectangle.
   - Properly handles cases where width or height is zero.

4. **String Representation**
   - [3-rectangle.py](./3-rectangle.py)
   - Enhances the rectangle class with a `__str__` method.
   - Displays the rectangle using '#' characters.
   - Returns an empty string if width or height is zero.

5. **Eval is Magic**
   - [4-rectangle.py](./4-rectangle.py)
   - Introduces a `__repr__` method to provide a string representation of the rectangle.

6. **Detect Instance Deletion**
   - [5-rectangle.py](./5-rectangle.py)
   - Adds a `__del__` method to print a farewell message when a rectangle instance is deleted.

7. **How Many Instances**
   - [6-rectangle.py](./6-rectangle.py)
   - Implements a class attribute `number_of_instances` to count instances created and deleted.
   - Increments and decrements this count accordingly.

8. **Change Representation**
   - [7-rectangle.py](./7-rectangle.py)
   - Introduces a public class attribute `class_symbol` to customize the string representation symbol.
   - Initially set to '#', but can be modified as needed.

9. **Compare Rectangles**
   - [8-rectangle.py](./8-rectangle.py)
   - Defines a static method `bigger_or_equal(rect_1, rect_2)` to compare rectangles based on area.
   - Raises a `TypeError` if inputs are not valid Rectangle instances.

10. **A Square is a Rectangle**
    - [9-rectangle.py](./9-rectangle.py)
    - Introduces a class method `square(cls, size=0)` to create square instances.
    - Inherits from the Rectangle class and sets width and height to the same value (size).

11. **N Queens**
    - [101-nqueens.py](./101-nqueens.py)
    - A Python program that solves the N queens puzzle.
    - Usage: `./101-nqueens.py N`
    - Validates input arguments, ensuring N is an integer and at least 4.
    - Finds and prints solutions for placing N non-attacking queens on an NxN chessboard.
