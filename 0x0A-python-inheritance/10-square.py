#!/usr/bin/python3
"""
Module for Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square inherites from rectangle """
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return super().area()
