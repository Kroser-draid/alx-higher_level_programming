#!/usr/bin/python3
def uniq_add(my_list=[]):
    appearance = []
    result = 0
    for item in my_list:
        if appearance.count(item) <= 0:
            result += item
            appearance.append(item)
    return result
