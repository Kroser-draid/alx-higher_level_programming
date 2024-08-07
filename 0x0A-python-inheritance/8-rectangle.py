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
            exit()
        else:
            self.__width = width
            self.__height = height
