#!/usr/bin/python3
"""
Module of a function that decode a document to string
"""
import json


def from_json_string(my_str):
    """ function that decode a document to string """
    return json.loads(my_str)
