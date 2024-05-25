#!/usr/bin/python3
"""
class square
"""


class Square:
    """
    class square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for n in range(self.__size):
                    print("#", end='')
                print("")

    def __str__(self):
        message = ""
        if self.__size == 0:
            message += "\n"
        else:
            for i in range(self.__position[1]):
                message += "\n"
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    message += " "
                for n in range(self.__size):
                    message += "#"
                message += "\n"
        return message.rstrip("\n")
