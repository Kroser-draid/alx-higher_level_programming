#!/usr/bin/python3

def multiple_returns(sentence):
    _len = len(sentence)
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    tuple_return = (_len, char)
    return tuple_return
