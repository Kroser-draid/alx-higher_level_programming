#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        message = "Exception: {}\n".format(e)
        sys.stderr.write(message)
        return False
