#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    length = 0
    try:
        for i in my_list:
            length += 1
    except IndexError:
        pass
    for j in range(length):
        if j < x:
            print(my_list[j], end='')
            result += 1
        else:
            break
    print('')
    return result
