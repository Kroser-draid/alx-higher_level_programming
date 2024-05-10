#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        i = len(my_list)
        for j in reversed(range(i)):
            print("{:d}".format(my_list[j]))
