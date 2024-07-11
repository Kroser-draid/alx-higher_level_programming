#!/usr/bin/python3
"""
Module of a function that returns a representation of a json file
"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
