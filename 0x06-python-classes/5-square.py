#!/usr/bin/python3
"""class square
"""


class Square:
    """class square
    """
    def __init__(self, size=0):
        """size init

        Args:
            size (integer):size of the square must be int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        size_square = self.__size
        if size_square == 0:
            print("")
        else:
            for i in range(size_square):
                for j in range(size_square):
                    print("#", end="")
                print("")
