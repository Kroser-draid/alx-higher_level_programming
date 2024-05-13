#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        factor = 0
        multi = 0
        for item in my_list:
            for i in range(len(item) - 1):
                multi += item[i] * item[i + 1]
                factor += item[i + 1]
        result = multi / factor
        return result
                