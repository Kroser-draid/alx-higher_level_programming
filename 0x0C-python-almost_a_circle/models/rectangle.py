#!/usr/bin/python3
""" module for rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherited from base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize of rectangle class """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """ setter for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ getter property for width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ setter property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ getter property for height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """ x setter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x getter """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ setter for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ y getter """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ function that returns value of rectangle instance """
        return self.__height * self.__width
