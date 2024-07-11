#!/usr/bin/python3
"""
Module for function that append to a file
"""


def append_write(filename="", text=""):
    """ function that append to file in the utf-8 encoding """
    with open(filename, "a", encoding="UTF-8") as file:
        chars = file.write(text)
    return chars
