#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        rem = number % -10
    else:
        rem = number % 10
    if rem < 0:
        rem *= -1
    print("{:d}".format(rem), end="")
    return rem
