#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        width = self.__width
        height = self.__height
        message = ""
        if width == 0 or height == 0:
            return ""
        else:
            for i in range(height):
                for j in range(width):
                    message += "#"
                if i < (height - 1):
                    message += "\n"
            return str(message)

    def __repr__(self):
        message = "Rectangle({}, {})".format(self.__width, self.__height)
        return message
