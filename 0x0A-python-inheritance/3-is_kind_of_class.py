#!/usr/bin/python3
"""
Module
"""


def is_kind_of_class(obj, a_class):
    """
    function of module
    """
    if isinstance(obj, a_class) or isinstance(type(obj), a_class):
        return True
    else:
        return False
