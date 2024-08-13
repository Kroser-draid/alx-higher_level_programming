#!/usr/bin/python3
""" module for pascal triangle function """


def pascal_triangle(n):
    """ pascal triangle function returns a list of list """
    if (n <= 0):
        return [[]]
    result = [[1]]

    for i in range(n):
        if (i != 0):
            result.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j] + result[i - 1][j - 1])

    return result
