#!/usr/bin/python3
"""
Module of a function that returns a representation of a json file
"""
import json


def to_json_string(my_obj):
    """ function that returns a representation of a json file """
    return json.dumps(my_obj)
