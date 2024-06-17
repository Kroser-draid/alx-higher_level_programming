#!/usr/bin/python3
"""
Module for checking inheretence
"""


def inherits_from(obj, a_class):
    """
    return true if it inherits
    returns false otherwise
    """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        False
