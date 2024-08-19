#!/usr/bin/python3
""" Module for base Class """


class Base:
    """ Base class """
    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            self.__nb_objects++
            id = self.__nb_objects
