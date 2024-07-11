#!/usr/bin/python3
"""
Module rectangle
"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """ rectangle class that inherites from basegeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area method """
        return self.__width * self.__height

    def __str__(self):
        """ str() will return the following """
        return "[{}] {}/{}".format(str(self.__class__.__name__), self.__width, self.__height)
