#!/usr/bin/python3
"""
square class
"""


class Square:
    """
    square class
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, another_square):
        if self.area() == another_square.area():
            return True
        else:
            return False

    def __lt__(self, another_square):
        if self.area() < another_square.area():
            return True
        else:
            return False

    def __le__(self, another_square):
        if self.area() <= another_square.area():
            return True
        else:
            return False

    def __gt__(self, another_square):
        if self.area() > another_square.area():
            return True
        else:
            return False

    def __ge__(self, another_square):
        if self.area() >= another_square.area():
            return True
        else:
            return False

        def __ne__(self, another_square):
            if self.area() != another_square.area():
                return True
            else:
                return False
