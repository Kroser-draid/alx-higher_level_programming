#!/usr/bin/python3
"""
module for class BaseGeometry
"""


class BaseGeometry:
    """
    basegeometry class
    """
    def __init__(self):
        pass

    def area(self):
        """area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates a value as an integer"""
        if type(value) is not type(7):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
