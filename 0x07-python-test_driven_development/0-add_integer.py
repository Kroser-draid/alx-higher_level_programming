#!/usr/bin/python3
"""
adding module
"""


def add_integer(a, b=98):
    """Returns a + b

        works with numbers:

        >>> add_integer(2, 3)
        5

        and strings:

        >>> add_integer("a", 3)
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer

        >>> add_integer(2, "a")
        Traceback (most recent call last):
        ...
        TypeError: b must be an integer

        and floats:

        >>> add_integer(2.2, 3)
        5

        >>> add_integer(2, 3.2)
        5

        """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
