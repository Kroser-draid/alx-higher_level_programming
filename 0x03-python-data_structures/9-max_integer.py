#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        MAXX = my_list[0]
        for i in range(len(my_list)):
            if MAXX < my_list[i]:
                MAXX = my_list[i]
    return MAXX