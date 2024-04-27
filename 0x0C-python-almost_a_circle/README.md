# Python - Rectangle and Square Project

In this Python project, I've implemented a system for working with rectangles and squares using object-oriented programming principles. The project includes three connected classes, a testing suite, and functionality to serialize and deserialize objects to/from JSON and CSV formats.

## Project Overview

The project is structured as follows:

### Classes :page_facing_up:

#### Base
- Represents the base class for all other classes in the project.
- Includes private class attribute `__nb_objects`.
- Defines public instance attribute `id`.
- Implements class constructor, static methods, class methods, and static method `draw`.

#### Rectangle
- Represents a rectangle.
- Inherits from the `Base` class.
- Defines private instance attributes `__width`, `__height`, `__x`, and `__y`.
- Implements class constructor, public methods for area and display, `__str__` method, and methods for updating and converting to a dictionary.

#### Square
- Represents a square.
- Inherits from the `Rectangle` class.
- Implements a class constructor, `__str__` method, methods for updating, and converting to a dictionary.

### Tests :white_check_mark:

The project includes a testing suite with the following test files:
- [test_base.py](./tests/test_models/test_base.py): Tests for the `Base` class.
- [test_rectangle.py](./tests/test_models/test_rectangle.py): Tests for the `Rectangle` class.
- [test_square.py](./tests/test_models/test_square.py): Tests for the `Square` class.

The tests cover various aspects of the project's functionality, ensuring correctness and robustness.

## Key Features

The project demonstrates proficiency in various Python concepts and tools, including:
- Object-oriented programming
- Exception handling
- Private attributes
- Getter and setter methods
- Class and static methods
- Inheritance
- File I/O
- `args` and `kwargs`
- JSON and CSV serialization/deserialization
- Unit testing using the `unittest` module

## Usage

You can use the classes provided in this project to work with rectangles and squares in your Python applications. The classes are designed to handle various operations and data conversions seamlessly.
