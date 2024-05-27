#!/usr/bin/python3
"""
say my name Module
"""


def say_my_name(first_name, last_name=""):
    """
    function that print my name is firstname lastname
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if len(first_name) == 0:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
