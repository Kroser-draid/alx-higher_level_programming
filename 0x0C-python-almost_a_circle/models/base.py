#!/usr/bin/python3
# base.py
"""Defines a base model class."""


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            self.__nb_objects++
            id = self.__nb_objects
