#!/usr/bin/python3
"""
doc
"""


def matrix_divided(matrix, div):
    int_float = "matrix must be a matrix (list of lists) of integers/floats"
    message_1 = "Each row of the matrix must have the same size"
    message_2 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(int_float)
    elif len(matrix) < 2:
        raise TypeError(int_float)
    else:
        first_len = len(matrix[0])
        for i in range(len(matrix)):
            if len(matrix[i]) != first_len:
                raise TypeError(message_1)
            for j in range(len(matrix[i])):
                if not isinstance(matrix[i][j], (int, float)):
                    raise TypeError(message_2)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(round((matrix[i][j] / div), 2))

    return new_matrix
