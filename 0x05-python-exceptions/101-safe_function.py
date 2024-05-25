#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        message = "Exception: {}\n".format(e)
        sys.stderr.write(message)
        return None
