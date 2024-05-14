#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e_message:
        error_msg = "Exception: " + str(e_message)
        sys.stderr.write(error_msg)
        return False
