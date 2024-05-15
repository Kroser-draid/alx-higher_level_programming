#!/usr/bin/python3
"""a rectangle class
"""


class Rectangle:
    """a rectangle class
    """
    def __init__(self, width=0, height=0):
        """pass
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.height

    def perimeter(self):
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return (self.__height + self.width) * 2
