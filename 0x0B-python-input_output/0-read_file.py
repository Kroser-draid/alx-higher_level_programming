#!/usr/bin/python3
"""
module for a function that read data from a file
"""


def read_file(filename=""):
    """ function that read data and print it from a file """
    with open(filename, "r", encoding="UTF-8") as file:
        data = file.read()
        print(data, end='')
