#!/usr/bin/python3
"""
Module for a function that load from a json file
"""
import json


def load_from_json_file(filename):
    """ function that load from a json file """
    with open(filename, "r", encoding='UTF-8') as file:
        return json.load(file)
