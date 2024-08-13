#!/usr/bin/python3
""" module for a function append after """


def append_after(filename="", search_string="", new_string=""):
    """ function """
    new_reel = []
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
