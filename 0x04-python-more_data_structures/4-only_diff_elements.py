#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = {x for x in set_1 if x not in set_2}
    for i in set_2:
        if i not in set_1:
            result.add(i)
    return result
