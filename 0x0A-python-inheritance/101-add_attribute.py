#!/usr/bin/python3
"""
function that add attributes
"""


def add_attribute(cls, attr, value):
    if '__dict__' not in dir(cls) or '__slots__' in dir(cls):
        raise TypeError('can\'t add new attribute')
    else:
        setattr(cls, attr, value)
