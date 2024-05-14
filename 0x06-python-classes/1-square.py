#!/usr/bin/python3
"""square class that have one private object
"""


class Square:
    """this is a square that defines a square
    """
    __size = 0

    def __init__(self, size):
        """this initiate the size arg

        Args:
            size (integer): The size of the square
        """
        self.__size = size
