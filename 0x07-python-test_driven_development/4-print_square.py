#!/usr/bin/python3
"""
print square Module
"""


def print_square(size):
    """
    print square of #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
