#!/usr/bin/python3
""" module for a function """


def class_to_json(obj):
    """ function that returns json serialazition of an obj """
    if isinstance(obj, dict):
        return "{" + ", ".join(f'"{k}": {class_to_json(v)}'
                               for k, v in obj.items()) + "}"
    elif isinstance(obj, list):
        return "[" + ", ".join(class_to_json(item)
                               for item in obj.items()) + "]"
    elif isinstance(obj, str):
        return '"{obj}"'
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif obj is None:
        return "null"
