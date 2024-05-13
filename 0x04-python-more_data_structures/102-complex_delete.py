#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        keys = []
        for j in a_dictionary.keys():
            keys.append(j)
        for i in range(len(keys)):
            item = keys[i]
            if a_dictionary[item] == value:
                del a_dictionary[item]
        return a_dictionary
    else:
        return a_dictionary
