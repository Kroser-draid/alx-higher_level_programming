#!/usr/bin/python3
"""
Module for a function that write in a file in utf-8 encoding
"""


def write_file(filename="", text=""):
    """ function that write to a file """
    with open(filename, "w", encoding='UTF-8') as file:
        chars = file.write(text)
    return chars
