#!/usr/bin/python3
"""
Module for a function that save to a json file
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that save to a json file """
    with open(filename, "w", encoding='UTF-8') as file:
        return json.dump(my_obj, file)
