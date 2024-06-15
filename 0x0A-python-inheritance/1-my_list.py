#!/usr/bin/python3
"""
List Module
"""


class MyList(list):
    """
    class inh from list
    """
    def print_sorted(self):
        print(sorted(self))
