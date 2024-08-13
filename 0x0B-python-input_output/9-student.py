#!/usr/bin/python3
""" module of a student clss """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return rep """
        ser_obj = {}

        for k, v in self.__dict__.items():
            if isinstance(v, (dict, list, str, int, bool)):
                ser_obj[k] = v

        return ser_obj
