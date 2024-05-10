#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        f_chr = None
        length = len(sentence)
        return (length, f_chr)
    else:
        f_chr = sentence[0]
        length = len(sentence)
        return (length, f_chr)
