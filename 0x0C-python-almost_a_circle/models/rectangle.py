#!/usr/bin/python3
""" module for rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherited from base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize of rectangle class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ setter for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ getter property for width """
        self.__width = width

    @property
    def height(self):
        """ setter property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ getter property for height """
        self.__height = height

    @property
    def x(self):
        """ x setter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x getter """
        self.__x = x

    @property
    def y(self):
        """ setter for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ y getter """
        self.__y = y
