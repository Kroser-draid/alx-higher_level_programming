#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    prev_value = 0
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        if char not in Roman:
            return None
        current_value = Roman[char]
        if current_value <= prev_value:
            num += current_value
        else:
            num = current_value - prev_value
        prev_value = current_value
    return num
