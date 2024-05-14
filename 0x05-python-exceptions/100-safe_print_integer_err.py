#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e_message:
        sys.stderr.write("Exception: {}".format(e_message))
        return False
    else:
        return True
