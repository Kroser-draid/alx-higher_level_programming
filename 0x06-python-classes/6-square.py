#!/usr/bin/python3
"""class square
"""


class Square:
    """class square
    """

    def __init__(self, size=0, postion=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(postion, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(postion) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(postion[0], int) and isinstance(postion[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif postion[0] < 0 or postion[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = postion

    def area(self):
        return self.__size * self.__size

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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for n in range(self.__position[1]):
                print("")
            for i in range(self.size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
