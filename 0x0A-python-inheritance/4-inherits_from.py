#!/usr/bin/python3
"""
Module for checking inheretence
"""


def inherits_from(obj, a_class):
    """
    return true if it inherits
    returns false otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
