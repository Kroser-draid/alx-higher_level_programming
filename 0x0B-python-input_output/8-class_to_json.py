#!/usr/bin/python3
""" module for a function """


def class_to_json(obj):
    """ function that returns json serialazition of an obj """

    serial_obj = {}

    for k, v in obj.__dict__.items():
        if isinstance(v, (int, bool, list, dict, str)):
            serial_obj[k] = v

    return serial_obj
