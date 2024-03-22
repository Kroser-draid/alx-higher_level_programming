#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    prev_value = 0
    for numeral in reversed(roman_string):
        value = dic[numeral]
        if value >= prev_value:
            decimal_value += value
        else:
            decimal_value -= value
        prev_value = value
    return decimal_value
