#!/usr/bin/python3
"""
Module rectangle
"""
bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """ rectangle class that inherites from basegeometry """
    def __init__(self, width, height):
        try:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        else:
            self.__width = width
            self.__height = height

    def area(self):
        """ area method """
        return self.__width * self.__height

    def __str__(self):
        """ str() will return the following """
        return f"[Rectangle] {self.__width}/{self.__height}"
