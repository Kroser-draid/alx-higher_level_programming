#!/usr/bin/python3
"""
Module for class MyInt
"""


class MyInt(int):
    """ class MyInt is a rebel has eq and ne reversed """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
