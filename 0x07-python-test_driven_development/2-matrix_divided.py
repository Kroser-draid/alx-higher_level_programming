#!/usr/bin/python3
"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    Args:
    matrix: A list of lists of integers or floats.
    div: A number (integer or float) by which to divide the matrix elements.
    Returns:
    A new matrix with all elements divided by div, rounded to 2 decimal places.
    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If rows of the matrix are not the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    message_2 = "Each row of the matrix must have the same size"
    message_3 = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list)
            and all(isinstance(row, list) for row in matrix)):
        raise TypeError(message_1)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(message_2)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message_3)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
